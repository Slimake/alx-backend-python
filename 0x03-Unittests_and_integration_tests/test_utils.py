#!/usr/bin/env python3
"""test_utils
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class for that inherit from unittest.TestCase
    """
    @parameterized.expand([
        ("test_case_1", {"a": 1}, ("a",), 1),
        ("test_case_2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test_case_3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected) -> None:
        """Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
