import unittest
from src import main

class TestMain(unittest.TestCase):
    def test_main_function_exists(self):
        self.assertIsNotNone(main.main)