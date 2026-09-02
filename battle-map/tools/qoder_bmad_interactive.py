#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path
import urllib.request

DEFAULT_MODEL = "Qwen3.8-Max"
DEFAULT_PROXY = "http://127.0.0.1:9939"
DEFAULT_STATUS = "http://127.0.0.1:28080/api/status"


def build_env(base, proxy=DEFAULT_PROXY):
    env = dict(base)
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
        env[key] = proxy
    return env


def build_launch_argv(model=DEFAULT_MODEL, add_dirs=None):
    argv = [
        "qodercli",
        "--model", model,
        "--permission-mode", "bypass_permissions",
    ]
    for directory in add_dirs or []:
        argv.extend(["--add-dir", directory])
    return argv


def preflight(status_url=DEFAULT_STATUS):
    with urllib.request.urlopen(status_url, timeout=3) as response:
        status = json.load(response)
    if status.get("engine_running") is not True:
        raise SystemExit("QoderVIP engine is not running")
    quota = status.get("quota") or {}
    if quota.get("has_active") is False:
        raise SystemExit("QoderVIP has no active entitlement")
    return status


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--proxy", default=DEFAULT_PROXY)
    parser.add_argument("--add-dir", action="append", default=[])
    args = parser.parse_args()

    project = Path(args.project).resolve()
    preflight()
    argv = build_launch_argv(args.model, args.add_dir)
    env = build_env(os.environ, args.proxy)
    os.chdir(project)
    os.execvpe(argv[0], argv, env)


if __name__ == "__main__":
    main()
