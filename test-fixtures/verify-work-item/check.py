#!/usr/bin/env python3
import pathlib
import sys

mode = sys.argv[1]
if mode == "pass":
    print("PASS fixture")
    raise SystemExit(0)
if mode == "fail-until-flag":
    if pathlib.Path("repair.pass").exists():
        print("PASS repaired fixture")
        raise SystemExit(0)
    print("FAIL expected fixture")
    raise SystemExit(1)
if mode == "mutate-restore":
    path = pathlib.Path("state/value.txt")
    original = path.read_bytes()
    path.write_text("temporary mutation\n", encoding="utf-8")
    path.write_bytes(original)
    print("PASS restored fixture")
    raise SystemExit(0)
raise SystemExit(3)
