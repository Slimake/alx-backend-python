#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines at the same time with async
    Return the sorted delays"""
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
