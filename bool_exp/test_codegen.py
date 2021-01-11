#!/usr/bin/python3
import unittest
from codegen import codegen


class TestCodegen(unittest.TestCase):
    def setUp(self):
        self.postfix = ['FAUX', 'VRAI', 'OU']
        self.last_postfix_elem = self.postfix[-1]
        self.first_postfix_elem = self.postfix[0]

    def test_is_postfix_is_a_list(self):
        self.assertIsInstance(self.postfix, list)

    def test_if_last_elem_is_an_operator(self):
        self.assertIn(self.last_postfix_elem, ['OU', 'ET'])

    def test_if_first_elem_is_a_digit(self):
        self.assertIn(self.first_postfix_elem, ['VRAI', 'FAUX'])


if  __name__ == "__main__":
    unittest.main()
