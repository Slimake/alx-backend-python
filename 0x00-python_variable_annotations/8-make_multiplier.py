#!/usr/bin/env python3
"""Module 8-make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def mul(multiply: float) -> float:
        return multiplier * multiply
    return mul
