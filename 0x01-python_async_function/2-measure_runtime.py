#!/usr/bin/env python3
"""2-measure_runtime.py"""

import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """
    Create a measure_time function with integers n and max_delay as
    arguments that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.
    """
    delays = asyncio.run(wait_n(n, max_delay))
    total_time = 0
    for delay in delays:
        total_time += delay
    return total_time / n
