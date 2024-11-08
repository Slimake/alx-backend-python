#!/usr/bin/env python3
"""test_utils Module
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Any


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class for that inherit from unittest.TestCase
    """
    @parameterized.expand([
        ("test_case_1", {"a": 1}, ("a",), 1),
        ("test_case_2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test_case_3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
      self, name: Any,
      nested_map: Any,
      path: Any,
      expected: Any) -> None:
        """Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("test_case_1", {}, ("a",)),
        ("test_case_2", {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
      self, name: Any,
      nested_map: Any,
      path: Any):
        """Test access_nested_map function to raise KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
