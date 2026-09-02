#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path
import shlex
import subprocess
import urllib.request

DEFAULT_MODEL = "Qwen3.8-Max"
DEFAULT_PROXY = "http://127.0.0.1:9939"
DEFAULT_STATUS = "http://127.0.0.1:28080/api/status"


def build_env(base, proxy=DEFAULT_PROXY):
    env = dict(base)
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
        env[key] = proxy
    return env


def runtime_name(skill_name):
    prefix = "bmad-agent-"
    if not skill_name.startswith(prefix):
        raise ValueError(f"not a BMAD agent skill: {skill_name}")
    return "bmad-" + skill_name[len(prefix):]


def _split_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta, text[end + 5:]


def compile_agent(project, skill_name):
    project = Path(project).resolve()
    skill_root = project / ".qoder" / "skills" / skill_name
    source = skill_root / "SKILL.md"
    meta, body = _split_frontmatter(source.read_text(encoding="utf-8"))
    body = body.replace("{project-root}", str(project))
    body = body.replace("{skill-root}", str(skill_root))
    body = body.replace("{skill-name}", skill_name)
    name = runtime_name(skill_name)
    out = project / ".qoder" / "agents" / f"{name}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    description = meta.get("description") or f"Runtime projection of {skill_name}"
    initial = (
        "Activate fully according to your BMAD activation protocol, present your "
        "resolved menu, and stop. Do not start a workflow unless the initial "
        "request explicitly selects one."
    )
    header = [
        "---",
        f"name: {name}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "permissionMode: bypassPermissions",
        "model: inherit",
        f"initialPrompt: {json.dumps(initial, ensure_ascii=False)}",
        "---",
    ]
    out.write_text("\n".join(header) + "\n\n" + body.lstrip(), encoding="utf-8")
    return out


def build_launch_argv(agent_name, model=DEFAULT_MODEL):
    return [
        "qodercli",
        "--agent", agent_name,
        "--model", model,
        "--permission-mode", "bypass_permissions",
    ]


def preflight(status_url=DEFAULT_STATUS):
    with urllib.request.urlopen(status_url, timeout=3) as response:
        status = json.load(response)
    if status.get("engine_running") is not True:
        raise SystemExit("QoderVIP engine is not running")
    quota = status.get("quota") or {}
    if quota.get("has_active") is False:
        raise SystemExit("QoderVIP has no active entitlement")
    return status


def launch(project, skill_name, model=DEFAULT_MODEL, proxy=DEFAULT_PROXY):
    project = Path(project).resolve()
    agent_path = compile_agent(project, skill_name)
    preflight()
    argv = build_launch_argv(agent_path.stem, model)
    return subprocess.run(argv, cwd=project, env=build_env(os.environ, proxy)).returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_name")
    parser.add_argument("--project", default=".")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--compile-only", action="store_true")
    args = parser.parse_args()
    agent_path = compile_agent(args.project, args.skill_name)
    print(agent_path)
    if args.compile_only:
        return 0
    preflight()
    argv = build_launch_argv(agent_path.stem, args.model)
    return subprocess.run(
        argv,
        cwd=Path(args.project).resolve(),
        env=build_env(os.environ),
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
