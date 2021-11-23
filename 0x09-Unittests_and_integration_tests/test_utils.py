#!/usr/bin/env python3
"""Flask App"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """class to test cases on utils.py"""

    @parameterized.expand([
                          ({"a": 1}, ('a',), 1)
                          ({"a": {"b": 2}}, ('a',), {'b': 2})
                          ({"a": {"b": 2}}, ('a', 'b'), 2)
                          ])
    def test_access_nested_map(self, n_map, path, ans):
        """Tests function with different situations with parameterized"""
        self.assertEqual(access_nested_map(nested_map, path), ans)


if __name__ == '__main__':
    unittest.main()
