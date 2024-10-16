#!/usr/bin/env python3
"""Module 100-safe_first_element"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the following code with the correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
