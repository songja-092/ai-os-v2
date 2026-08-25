#!/usr/bin/env python3
"""V2 Capability Lab: public-source audit and project-blind sandbox trials."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlparse


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PLUGIN_ROOT.parents[1]
DEFAULT_LAB = REPO_ROOT / "pm1-artifacts" / "capability-lab"
REGISTRY = PLUGIN_ROOT / "registry" / "capabilities.json"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")
GITHUB_PATH_RE = re.compile(r"^/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$")
RISK_PATTERNS = {
    "environment_access": r"process\.env|os\.environ|getenv\(",
    "home_access": r"\.ssh|\.config|\.claude|\.codex|homedir\(|Path\.home\(",
    "process_execution": r"child_process|execSync|spawn\(|subprocess\.|os\.system",
    "destructive_file_operation": r"rmSync|rmtree|unlinkSync|shutil\.rmtree",
    "external_upload_or_telemetry": r"telemetry|analytics|sentry|api\.[A-Za-z0-9.-]+",
    "install_lifecycle": r"preinstall|postinstall|prepare",
}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path, default: object | None = None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def validate_id(candidate_id: str) -> str:
    if not ID_RE.fullmatch(candidate_id):
        raise ValueError("candidate id must be lower-case kebab-case and at most 63 characters")
    return candidate_id


def validate_public_github(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme != "https" or parsed.hostname != "github.com" or parsed.username or parsed.password:
        raise ValueError("only credential-free public https://github.com/<owner>/<repo> URLs are allowed")
    if not GITHUB_PATH_RE.fullmatch(parsed.path):
        raise ValueError("GitHub source must point to one repository root")
    return source.rstrip("/")


def trial_dir(lab: Path, candidate_id: str) -> Path:
    return lab / "trials" / validate_id(candidate_id)


def source_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts):
        digest.update(str(path.relative_to(root)).encode())
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


def static_audit(source_dir: Path) -> dict:
    findings: list[dict] = []
    scanned = 0
    for path in sorted(p for p in source_dir.rglob("*") if p.is_file() and ".git" not in p.parts):
        if path.stat().st_size > 1_000_000:
            continue
        if path.suffix.lower() not in {".js", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".sh", ".json", ".md"}:
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for risk, pattern in RISK_PATTERNS.items():
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
            if matches:
                findings.append({
                    "risk": risk,
                    "file": str(path.relative_to(source_dir)),
                    "match_count": len(matches),
                })
    package = read_json(source_dir / "package.json", {}) or {}
    scripts = package.get("scripts", {}) if isinstance(package, dict) else {}
    lifecycle = {k: v for k, v in scripts.items() if k in {"preinstall", "install", "postinstall", "prepare"}}
    licenses = [str(p.relative_to(source_dir)) for p in source_dir.glob("LICENSE*") if p.is_file()]
    return {
        "scanned_text_files": scanned,
        "findings": findings,
        "package_lifecycle_scripts": lifecycle,
        "license_files": licenses,
        "automatic_execution_allowed": False,
        "note": "Findings require review; absence of a match is not a security guarantee.",
    }


def cmd_prepare(args: argparse.Namespace) -> None:
    lab = Path(args.lab).resolve()
    candidate_id = validate_id(args.id)
    source = validate_public_github(args.source)
    target = trial_dir(lab, candidate_id)
    if target.exists():
        raise FileExistsError(f"trial already exists: {target}")
    source_dir = target / "source"
    target.mkdir(parents=True)
    clone_env = {"PATH": os.environ.get("PATH", ""), "HOME": str(target / "empty-home"), "GIT_TERMINAL_PROMPT": "0"}
    subprocess.run([
        "git", "-c", "credential.helper=", "clone", "--depth", "1", "--no-tags", source, str(source_dir)
    ], check=True, env=clone_env)
    commit = subprocess.check_output(["git", "-C", str(source_dir), "rev-parse", "HEAD"], text=True).strip()
    audit = static_audit(source_dir)
    record = {
        "schema_version": "1.0",
        "candidate_id": candidate_id,
        "source": source,
        "source_class": "public_github",
        "prepared_at": now(),
        "source_commit": commit,
        "source_sha256": source_digest(source_dir),
        "status": "static_reviewed",
        "private_project_mounted": False,
        "audit": audit,
        "trials": [],
    }
    write_json(target / "record.json", record)
    print(json.dumps(record, ensure_ascii=False, indent=2))


def cmd_fixture(args: argparse.Namespace) -> None:
    lab = Path(args.lab).resolve()
    target = trial_dir(lab, args.id)
    record_path = target / "record.json"
    record = read_json(record_path)
    if not record:
        raise FileNotFoundError("prepare the candidate first")
    fixture = target / "fixture"
    fixture.mkdir(exist_ok=True)
    html = """<!doctype html><html lang=\"ko\"><meta charset=\"utf-8\"><title>Public Fixture</title>
<style>:root{--ink:#172033;--accent:#2f6fed;--space:16px}body{font-family:sans-serif;color:var(--ink);margin:0;padding:32px;background:#f6f8fb}.panel{max-width:760px;margin:auto;background:white;border:1px solid #ccd5e1;padding:24px}.actions{display:flex;gap:12px}button{padding:10px 16px}</style>
<main class=\"panel\"><p>GENERATED PUBLIC FIXTURE — NO PROJECT DATA</p><h1>프로젝트 작업실</h1><p>가짜 데이터로 후보 도구를 시험합니다.</p><div class=\"actions\"><button>미리보기</button><button>수정</button></div></main></html>"""
    (fixture / "index.html").write_text(html, encoding="utf-8")
    record["fixture"] = {"path_in_sandbox": "/work/fixture/index.html", "contains_private_project_data": False, "created_at": now()}
    write_json(record_path, record)
    print(json.dumps(record["fixture"], ensure_ascii=False, indent=2))


def sandbox_command(target: Path, network: str, command: list[str]) -> list[str]:
    if not shutil.which("bwrap"):
        raise RuntimeError("bubblewrap is required")
    args = ["bwrap", "--die-with-parent", "--new-session", "--unshare-all"]
    if network == "public":
        args.append("--share-net")
    for system_path in ("/usr", "/bin", "/lib", "/lib64", "/opt"):
        if Path(system_path).exists():
            args += ["--ro-bind", system_path, system_path]
    if network == "public":
        for network_path in ("/etc/resolv.conf", "/etc/ssl/certs", "/etc/hosts"):
            if Path(network_path).exists():
                args += ["--ro-bind", network_path, network_path]
    args += [
        "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--dir", "/home", "--dir", "/home/candidate",
        "--setenv", "HOME", "/home/candidate",
        "--setenv", "XDG_CONFIG_HOME", "/home/candidate/.config",
        "--setenv", "XDG_CACHE_HOME", "/tmp/cache",
        "--bind", str(target), "/work", "--chdir", "/work",
        "--", *command,
    ]
    return args


def cmd_trial(args: argparse.Namespace) -> None:
    lab = Path(args.lab).resolve()
    target = trial_dir(lab, args.id)
    record_path = target / "record.json"
    record = read_json(record_path)
    if not record or not record.get("fixture"):
        raise RuntimeError("prepare the candidate and generate the fixture first")
    if args.network == "public" and not args.approved_by_user:
        raise PermissionError("public-network trial requires --approved-by-user")
    command = list(args.command)
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        raise ValueError("a command is required after --")
    run = sandbox_command(target, args.network, command)
    clean_env = {"PATH": "/opt/codex-desktop/resources/node-runtime/bin:/usr/bin:/bin", "LANG": "C.UTF-8"}
    completed = subprocess.run(run, text=True, capture_output=True, timeout=args.timeout, env=clean_env)
    evidence_dir = target / "evidence"
    evidence_dir.mkdir(exist_ok=True)
    trial_id = f"trial-{len(record['trials']) + 1:03d}"
    (evidence_dir / f"{trial_id}.stdout.txt").write_text(completed.stdout, encoding="utf-8")
    (evidence_dir / f"{trial_id}.stderr.txt").write_text(completed.stderr, encoding="utf-8")
    result = {
        "trial_id": trial_id,
        "executed_at": now(),
        "network": args.network,
        "command": command,
        "returncode": completed.returncode,
        "private_project_mounted": False,
        "environment_credentials_forwarded": False,
        "stdout": f"evidence/{trial_id}.stdout.txt",
        "stderr": f"evidence/{trial_id}.stderr.txt",
    }
    record["trials"].append(result)
    record["status"] = "isolated_tested"
    write_json(record_path, record)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def load_registry() -> dict:
    return read_json(REGISTRY, {"schema_version": "1.0", "capabilities": []})


def cmd_adopt(args: argparse.Namespace) -> None:
    if not args.approved_by_user:
        raise PermissionError("adoption requires --approved-by-user")
    lab = Path(args.lab).resolve()
    target = trial_dir(lab, args.id)
    record = read_json(target / "record.json")
    if not record or record.get("status") != "isolated_tested":
        raise RuntimeError("candidate must complete an isolated trial before adoption")
    registry = load_registry()
    registry["capabilities"] = [c for c in registry["capabilities"] if c["candidate_id"] != args.id]
    registry["capabilities"].append({
        "candidate_id": args.id,
        "source": record["source"],
        "source_commit": record["source_commit"],
        "status": "adopted",
        "adapter_enabled": False,
        "core_write_allowed": False,
        "private_project_access": False,
        "adopted_at": now(),
        "trial_record": str((target / "record.json").relative_to(REPO_ROOT)),
        "removal": "disable adapter, preserve evidence, then run discard with user approval",
    })
    write_json(REGISTRY, registry)
    record["status"] = "adopted"
    write_json(target / "record.json", record)
    print(json.dumps(registry["capabilities"][-1], ensure_ascii=False, indent=2))


def cmd_discard(args: argparse.Namespace) -> None:
    if not args.approved_by_user:
        raise PermissionError("discard requires --approved-by-user")
    lab = Path(args.lab).resolve()
    target = trial_dir(lab, args.id)
    if not target.exists():
        raise FileNotFoundError(target)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    destination = lab / "discarded" / f"{args.id}-{stamp}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(target), destination)
    registry = load_registry()
    for capability in registry["capabilities"]:
        if capability["candidate_id"] == args.id:
            capability["status"] = "discarded"
            capability["adapter_enabled"] = False
            capability["discarded_at"] = now()
            capability["recoverable_path"] = str(destination.relative_to(REPO_ROOT))
    write_json(REGISTRY, registry)
    print(json.dumps({"status": "discarded", "recoverable_path": str(destination)}, ensure_ascii=False, indent=2))


def cmd_status(args: argparse.Namespace) -> None:
    lab = Path(args.lab).resolve()
    records = []
    for path in sorted((lab / "trials").glob("*/record.json")) if (lab / "trials").exists() else []:
        record = read_json(path)
        records.append({"candidate_id": record["candidate_id"], "status": record["status"], "source_commit": record["source_commit"]})
    print(json.dumps({"lab": str(lab), "active_trials": records, "registry": load_registry()}, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--lab", default=str(DEFAULT_LAB))
    commands = root.add_subparsers(dest="action", required=True)
    prepare = commands.add_parser("prepare")
    prepare.add_argument("--id", required=True)
    prepare.add_argument("--source", required=True)
    prepare.set_defaults(func=cmd_prepare)
    fixture = commands.add_parser("fixture")
    fixture.add_argument("--id", required=True)
    fixture.set_defaults(func=cmd_fixture)
    trial = commands.add_parser("trial")
    trial.add_argument("--id", required=True)
    trial.add_argument("--network", choices=("none", "public"), default="none")
    trial.add_argument("--approved-by-user", action="store_true")
    trial.add_argument("--timeout", type=int, default=60)
    trial.add_argument("command", nargs=argparse.REMAINDER)
    trial.set_defaults(func=cmd_trial)
    adopt = commands.add_parser("adopt")
    adopt.add_argument("--id", required=True)
    adopt.add_argument("--approved-by-user", action="store_true")
    adopt.set_defaults(func=cmd_adopt)
    discard = commands.add_parser("discard")
    discard.add_argument("--id", required=True)
    discard.add_argument("--approved-by-user", action="store_true")
    discard.set_defaults(func=cmd_discard)
    status = commands.add_parser("status")
    status.set_defaults(func=cmd_status)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
        return 0
    except (ValueError, RuntimeError, PermissionError, FileNotFoundError, FileExistsError, subprocess.SubprocessError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
