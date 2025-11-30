#!/usr/bin/env python3
import argparse
import os
import re
import sys
from pathlib import Path

from utils.dirs import ROOT_DIR


def latest_year() -> Path:
    return sorted(ROOT_DIR.rglob("[0-9]" * 4))[-1]


# TODO: make work for both 1, 01, 10, 20 14, 21 9, etc.
def latest() -> Path:
    year_dir = latest_year()
    ptr = re.compile(r".+\/[0-9][0-9]\..+")
    return sorted(f for f in year_dir.glob("*") if ptr.match(str(f)))[-1]


def normalize_target(arg: str | None) -> Path:
    """
    accept:
    - yyyy/dd.py
    - yyyy-dd
    - dd (defaults to current year)

    """
    if arg is None or len(arg.strip()) == 0:
        return latest()

    arg = arg.strip()
    if arg.endswith(".py"):
        p = Path(arg)
        if not p.exists():
            p = ROOT_DIR / arg
        if not p.exists():
            raise Exception(f"Path '{arg}' ('{p}') do not exists.")
        return p
    if "-" in arg:
        year, day = arg.split("-", 1)
        return ROOT_DIR / year / f"{day.zfill(2)}.py"
    return latest_year() / f"{arg.zfill(2)}.py"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--target", required=False, help="day spec like '2024-05', '05', or a path like '2024/05.py'"
    )
    parser.add_argument(
        "--args", required=False, default=[], nargs=argparse.REMAINDER, help="extra args passed to the day script"
    )
    pargs = parser.parse_args()

    script = normalize_target(pargs.target)
    if not script.exists():
        sys.stderr.write(f"Not found: {script}\n")
        return 1

    env = os.environ.copy()
    env["PYTHONPATH"] = ROOT_DIR.as_posix()

    cmd = [sys.executable, script.as_posix(), *pargs.args]
    return os.execve(sys.executable, cmd, env)


if __name__ == "__main__":
    raise SystemExit(main())
