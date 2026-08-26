#!/usr/bin/env python3
"""Append 3–5 genuinely new visual references while preserving prior state."""

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json_atomic(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as target:
        json.dump(payload, target, ensure_ascii=False, indent=2)
        target.write("\n")
        temp_path = target.name
    os.replace(temp_path, path)


def image_dhash(path):
    with Image.open(path) as image:
        pixels = image.convert("L").resize((9, 8)).tobytes()
    bits = 0
    for row in range(8):
        for column in range(8):
            bits = (bits << 1) | (pixels[row * 9 + column] > pixels[row * 9 + column + 1])
    return bits


def hamming(left, right):
    return (left ^ right).bit_count()


def coverage(items):
    return {
        "total": len(items),
        "korean": sum(item.get("region") == "korea" for item in items),
        "actual_service": sum("actual_service" in item.get("source_type", "") for item in items),
        "user_provided": sum(item.get("source_type") == "user_provided" for item in items),
    }


def load_collector(path):
    spec = importlib.util.spec_from_file_location("pm4_visual_reference_collector", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--collection", required=True)
    parser.add_argument("--image-dir", required=True)
    parser.add_argument("--review-output", required=True)
    parser.add_argument("--regional-seed-file", required=True)
    parser.add_argument("--discovery-script", required=True)
    parser.add_argument("--collector-script", required=True)
    parser.add_argument("--append-limit", type=int, default=5)
    args = parser.parse_args()

    if not 3 <= args.append_limit <= 5:
        raise SystemExit("Refill은 한 번에 새 후보 3~5개만 추가할 수 있습니다.")
    lock_path = args.state + ".refill.lock"
    try:
        lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.write(lock_fd, str(os.getpid()).encode("ascii"))
        os.close(lock_fd)
    except FileExistsError:
        raise SystemExit("추가 탐색이 이미 실행 중입니다.")
    try:
        return run_refill(args)
    finally:
        try:
            os.unlink(lock_path)
        except OSError:
            pass


def run_refill(args):
    previous = read_json(args.state)
    collection = read_json(args.collection)
    if previous.get("request_id") != collection.get("request_id"):
        raise SystemExit("상태와 수집 결과의 요청이 다릅니다.")
    previous_items = previous.get("items", [])
    round_number = int(previous.get("refill", {}).get("round", 0)) + 1
    existing_urls = {item["source_url"] for item in previous_items}
    existing_hashes = {item["sha256"] for item in previous_items}
    existing_visual_hashes = [(item["reference_id"], image_dhash(item["local_image_path"])) for item in previous_items]
    discarded_ids = {key for key, value in previous.get("decisions", {}).items() if value == "discard"}
    discarded_visual_hashes = [value for key, value in existing_visual_hashes if key in discarded_ids]

    with tempfile.TemporaryDirectory(prefix="pm4-refill-") as temp_dir:
        seeds_path = os.path.join(temp_dir, "seeds.json")
        captured_path = os.path.join(temp_dir, "captured.json")
        temp_images = os.path.join(temp_dir, "images")
        discovery = subprocess.run([
            args.discovery_script,
            "--receipt", args.receipt,
            "--output", seeds_path,
            "--limit", str(max(args.append_limit * 3, 10)),
            "--regional-seed-file", args.regional_seed_file,
            "--exclude-file", args.state,
            "--refill-round", str(round_number),
        ], text=True, capture_output=True)
        if discovery.returncode not in {0, 2} or not os.path.exists(seeds_path):
            raise SystemExit(discovery.stderr.strip() or "새 Reference 탐색에 실패했습니다.")
        subprocess.run([
            args.collector_script,
            "--receipt", args.receipt,
            "--seed-file", seeds_path,
            "--output", captured_path,
            "--image-dir", temp_images,
        ], check=True, stdout=subprocess.DEVNULL)
        discovered = read_json(seeds_path)
        captured = read_json(captured_path)

        accepted = []
        deduplicated = []
        visual_hashes = list(existing_visual_hashes)
        for item in captured.get("items", []):
            reason = None
            if item["source_url"] in existing_urls:
                reason = "duplicate_url"
            elif item["sha256"] in existing_hashes:
                reason = "duplicate_image_hash"
            else:
                candidate_hash = image_dhash(item["local_image_path"])
                nearest = min((hamming(candidate_hash, value) for _, value in visual_hashes), default=64)
                discarded_nearest = min((hamming(candidate_hash, value) for value in discarded_visual_hashes), default=64)
                if discarded_nearest <= 5:
                    reason = "visually_similar_to_discarded"
                elif nearest <= 3:
                    reason = "visually_similar_to_existing"
            if reason:
                deduplicated.append({"reference_id": item["reference_id"], "reason": reason})
                continue
            final_name = f"refill-r{round_number:02d}-{len(accepted) + 1:02d}-{item['sha256'][:12]}{Path(item['local_image_path']).suffix}"
            final_path = os.path.join(args.image_dir, final_name)
            os.makedirs(args.image_dir, exist_ok=True)
            shutil.copy2(item["local_image_path"], final_path)
            item["local_image_path"] = os.path.abspath(final_path)
            item["reference_id"] = f"ref-refill-r{round_number:02d}-{len(accepted) + 1:02d}"
            item["refill_round"] = round_number
            accepted.append(item)
            existing_urls.add(item["source_url"])
            existing_hashes.add(item["sha256"])
            visual_hashes.append((item["reference_id"], image_dhash(final_path)))
            if len(accepted) >= args.append_limit:
                break

        if len(accepted) < 3:
            for item in accepted:
                try:
                    os.unlink(item["local_image_path"])
                except OSError:
                    pass
            raise SystemExit("새롭고 중복되지 않은 Reference를 3개 이상 확보하지 못했습니다. 기존 목록은 유지됩니다.")

        merged = json.loads(json.dumps(previous))
        merged["items"] = previous_items + accepted
        merged["coverage"] = coverage(merged["items"])
        merged["source_failures"] = previous.get("source_failures", []) + captured.get("source_failures", [])
        merged["decisions"] = previous.get("decisions", {})
        merged["revision"] = int(previous.get("revision", 1)) + 1
        merged["last_action"] = "visual-reference.refill"
        merged["refill"] = {
            "round": round_number,
            "added_count": len(accepted),
            "added_reference_ids": [item["reference_id"] for item in accepted],
            "queries": discovered.get("queries", []),
            "provider_failures": discovered.get("source_failures", []),
            "deduplicated": deduplicated,
            "dedup_methods": ["source_url", "sha256", "dhash_visual_similarity"],
            "decision_influence": discovered.get("previous_decision_influence", {}),
            "completed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        merged.setdefault("refill_history", []).append(merged["refill"])
        original_collection = Path(args.collection).read_bytes()
        original_state = Path(args.state).read_bytes()
        original_review = Path(args.review_output).read_bytes() if Path(args.review_output).exists() else None
        try:
            write_json_atomic(args.collection, merged)
            write_json_atomic(args.state, merged)
            collector = load_collector(args.collector_script)
            collector.render_review(args.review_output, args.collection, merged)
        except Exception:
            Path(args.collection).write_bytes(original_collection)
            Path(args.state).write_bytes(original_state)
            if original_review is not None:
                Path(args.review_output).write_bytes(original_review)
            for item in accepted:
                try:
                    os.unlink(item["local_image_path"])
                except OSError:
                    pass
            raise
        print(json.dumps({"round": round_number, "added": len(accepted), "total": len(merged["items"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
