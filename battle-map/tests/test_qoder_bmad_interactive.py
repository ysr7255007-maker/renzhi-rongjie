import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "tools" / "qoder_bmad_interactive.py"


class QoderBmadInteractiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("qoder_bmad_interactive", MODULE)
        cls.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.mod)

    def test_launch_argv_is_interactive_tui(self):
        argv = self.mod.build_launch_argv(
            "Qwen3.8-Max",
            ["/tmp/BMAD-METHOD", "/tmp/bmad-loop"],
        )
        self.assertEqual(argv[0], "qodercli")
        self.assertEqual(argv[argv.index("--model") + 1], "Qwen3.8-Max")
        self.assertIn("--permission-mode", argv)
        self.assertEqual(argv.count("--add-dir"), 2)
        for forbidden in ("-p", "-i", "--resume", "--session-id", "--output-format"):
            self.assertNotIn(forbidden, argv)

    def test_vip_environment_is_inherited(self):
        env = self.mod.build_env({}, "http://127.0.0.1:9939")
        for key in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            self.assertEqual(env[key], "http://127.0.0.1:9939")


if __name__ == "__main__":
    unittest.main()
