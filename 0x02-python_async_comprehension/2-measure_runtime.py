#!/usr/bin/env python3
"""2-measure_runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
    """
    tasks = [async_comprehension() for _ in range(4)]
    start_time = time.time()
    await asyncio.gather(*tasks)
    total_time = time.time() - start_time
    return total_time
