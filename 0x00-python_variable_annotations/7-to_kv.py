#!/usr/bin/env python3
"""Module 7-to_kv"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR
    float v as arguments and returns a tuple
    """
    return (k, v ** 2)
