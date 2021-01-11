#!/usr/bin/python3
import unittest
from scanner import scanner


class TestScanner(unittest.TestCase):
    def setUp(self):
        self.scan = "(1+2)*3"
        self.scanned = [
            ('PAR_OUV', '('),
            ('NOMBRE', '1'),
            ('OP', '+'),
            ('NOMBRE', '2'),
            ('PAR_FER', ')'),
            ('OP', '*'),
            ('NOMBRE', '3')
        ]

    def test_if_scanned_is_a_string(self):
        self.assertIsInstance(self.scan, str)

    def test_if_return_value_is_list(self):
        self.assertIsInstance(scanner(self.scan), list)

    def test_if_string_is_goodly_scanned(self):
        self.assertEqual(scanner(self.scan), self.scanned)


if  __name__ == "__main__":
    unittest.main()
