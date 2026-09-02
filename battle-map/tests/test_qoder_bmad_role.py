import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "tools" / "qoder_bmad_role.py"


class QoderBmadRoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("qoder_bmad_role", MODULE)
        cls.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.mod)

    def test_compile_projects_bmad_agent_skill_into_qoder_agent(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = root / ".qoder/skills/bmad-agent-analyst"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: bmad-agent-analyst\ndescription: Analyst role\n---\n"
                "ROOT={project-root}\nSKILL={skill-root}\nNAME={skill-name}\nROLE={agent.role}\n"
            )
            out = self.mod.compile_agent(root, "bmad-agent-analyst")
            text = out.read_text()
            self.assertIn("name: bmad-analyst", text)
            self.assertIn("permissionMode: bypassPermissions", text)
            self.assertIn(str(root), text)
            self.assertIn(str(skill), text)
            self.assertIn("NAME=bmad-agent-analyst", text)
            self.assertIn("ROLE={agent.role}", text)
            self.assertNotIn("{project-root}", text)
            self.assertNotIn("{skill-root}", text)
            self.assertNotIn("{skill-name}", text)

    def test_launch_argv_is_native_persistent_agent_tui(self):
        argv = self.mod.build_launch_argv("bmad-analyst", "Qwen3.8-Max")
        self.assertEqual(argv[0], "qodercli")
        self.assertIn("--agent", argv)
        self.assertEqual(argv[argv.index("--agent") + 1], "bmad-analyst")
        self.assertIn("--model", argv)
        self.assertIn("--permission-mode", argv)
        for forbidden in ("-p", "--resume", "--session-id", "--setting-sources"):
            self.assertNotIn(forbidden, argv)

    def test_vip_environment_is_inherited_by_persistent_session(self):
        env = self.mod.build_env({}, "http://127.0.0.1:9939")
        for key in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            self.assertEqual(env[key], "http://127.0.0.1:9939")


if __name__ == "__main__":
    unittest.main()
