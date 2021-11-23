#!/usr/bin/env python3
"""Flask App"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """class to test cases on utils.py"""

    @parameterized.expand([
        ({"a": 1}, ('a',), 1)
        ({"a": {"b": 2}}, ('a',), {'b': 2})
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, n_map, path, ans):
        self.assertEqual(access_nested_map(n_map, path), ans)


if __name__ == '__main__':
    unittest.main()
