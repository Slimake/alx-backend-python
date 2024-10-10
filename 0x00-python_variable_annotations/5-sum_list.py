#!/usr/bin/env python3
"""Module 5-sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of input_list"""
    result: float = 0.0
    for n in input_list:
        result += n

    return result
