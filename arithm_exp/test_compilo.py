#!/usr/bin/python3
import unittest
import os
from compilo import main

class TestCompilo(unittest.TestCase):
    def setUp(self):
        self.file = "exp.txt"

    def test_is_compiled(self):
        self.assertTrue(main(self.file))

    def test_is_param_string(self):
        self.assertIsInstance(self.file, str)

    def test_is_param_is_a_file(self):
        is_file = os.path.isfile(self.file)
        self.assertTrue(is_file)

    def test_is_param_is_not_a_file(self):
        is_not_a_file = os.path.isfile("self.file")
        self.assertFalse(is_not_a_file)


if  __name__ == "__main__":
    unittest.main()
