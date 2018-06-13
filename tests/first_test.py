import unittest
from contextlib import contextmanager
from unittest.mock import patch

from <your_app_entry_point> import main

@contextmanager
def env(env_dict, clear=True):
    with patch.dict("os.environ", env_dict, clear=clear):
        yield

class TestCLI(unittest.TestCase):

    def test_db_migration(self):
        with env(ENV_KEY1=env_value_1, ...):
            sys.argv = [<cli_entry_point_cmd>, "db", "upgrade"]
            with self.assertRaises(SystemExit) as exit:
                main()
            assert exit.exception.code == 0
