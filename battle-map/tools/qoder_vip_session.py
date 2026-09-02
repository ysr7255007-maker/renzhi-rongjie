#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import urllib.request

DEFAULT_PROXY = 'http://127.0.0.1:9939'
DEFAULT_STATUS = 'http://127.0.0.1:28080/api/status'


def build_env(base, proxy=DEFAULT_PROXY):
    env = dict(base)
    env.update({
        'HTTP_PROXY': proxy,
        'HTTPS_PROXY': proxy,
        'http_proxy': proxy,
        'https_proxy': proxy,
    })
    return env


def build_argv(mode, session_id, model, cwd, add_dirs, prompt):
    argv = [
        'qodercli', '-p', '--cwd', cwd,
        '--model', model,
        '--permission-mode', 'bypass_permissions',
        '--setting-sources', 'project',
        '--output-format', 'stream-json',
    ]
    for path in add_dirs:
        argv += ['--add-dir', path]
    argv += ['--resume' if mode == 'resume' else '--session-id', session_id, prompt]
    return argv


def preflight(status_url=DEFAULT_STATUS):
    with urllib.request.urlopen(status_url, timeout=3) as response:
        status = json.load(response)
    if status.get('engine_running') is not True:
        raise SystemExit('QoderVIP engine is not running')
    quota = status.get('quota') or {}
    if quota.get('has_active') is False:
        raise SystemExit('QoderVIP has no active entitlement')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=('start', 'resume'))
    p.add_argument('--session-id', required=True)
    p.add_argument('--model', required=True)
    p.add_argument('--cwd', required=True)
    p.add_argument('--add-dir', action='append', default=[])
    p.add_argument('--proxy', default=DEFAULT_PROXY)
    p.add_argument('prompt')
    args = p.parse_args()
    preflight()
    proc = subprocess.run(
        build_argv(args.mode, args.session_id, args.model, args.cwd, args.add_dir, args.prompt),
        cwd=args.cwd,
        env=build_env(os.environ, args.proxy),
    )
    raise SystemExit(proc.returncode)


if __name__ == '__main__':
    main()
