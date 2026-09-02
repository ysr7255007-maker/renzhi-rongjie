import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / 'tools' / 'qoder_vip_session.py'

class QoderVipSessionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('qoder_vip_session', MODULE)
        cls.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.mod)

    def test_start_and_resume_share_vip_proxy_environment(self):
        env = self.mod.build_env({}, 'http://127.0.0.1:9939')
        for key in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy'):
            self.assertEqual(env[key], 'http://127.0.0.1:9939')

    def test_resume_uses_resume_flag_not_new_session_id(self):
        argv = self.mod.build_argv('resume', 'session-1', 'Qwen3.8-Max', '/tmp/p', [], 'continue')
        self.assertIn('--resume', argv)
        self.assertNotIn('--session-id', argv)
        self.assertEqual(argv[argv.index('--resume') + 1], 'session-1')

if __name__ == '__main__':
    unittest.main()
