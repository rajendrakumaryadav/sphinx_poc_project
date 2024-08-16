import unittest
from pathlib import Path

from deep_learning_with_pytorch.data import connection


class ConnectionTest(unittest.TestCase):
    def test_get_connection(self):
        conn = connection.get_connection_path()

        self.assertEqual(
            conn,
            Path(
                "/home/rajendrayadav/Documents/deep_learning_with_pytorch/miscs"
            ),
        )
