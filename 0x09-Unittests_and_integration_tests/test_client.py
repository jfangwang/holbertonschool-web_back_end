#!/usr/bin/env python3
"""Flask App"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class to test cases in client.py"""

    @parameterized.expand([
                          ("google", {"payload": True}),
                          ("abc", {"payload": False})
                          ])
    @patch('client.get_json')
    def test_org(self, name, payload, get):
        """test github org client"""
        get.return_value = payload
        test = GithubOrgClient(name)
        output = test.org
        self.assertEqual(payload, output)
        get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
