#!/usr/bin/python3
import unittest
from parser import parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.ul = [('NOMBRE', '1'), ('OP', '+'), ('NOMBRE', '2')]
        self.ul_postfixed = ['1', '2', '+']

        self.parser_values = parser(self.ul)

    def test_if_param_is_a_list(self):
        self.assertIsInstance(self.ul, list)

    def test_if_parser_values_first_return_is_true(self):
        self.assertTrue(self.parser_values[0])

    def test_if_parser_values_second_return_is_list(self):
        self.assertIsInstance(self.parser_values[1], list)

    def test_if_parser_values_second_return_is_postfixed(self):
        self.assertEqual(self.ul_postfixed, self.parser_values[1])


if  __name__ == "__main__":
    unittest.main()
