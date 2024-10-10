#!/usr/bin/env python3
"""Modue 6-sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of mxd_lst as a float"""
    result: float = 0.0

    for num in mxd_lst:
        result += num
    return result
