#!/usr/bin/env python3
"""Task 2 solution."""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of concurrent executions.
        max_delay (int): Maximum delay value.

    Returns:
        float: Average execution time per iteration.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    avg = (end - start) / n
    return (avg)
