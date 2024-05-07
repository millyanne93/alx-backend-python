#!/usr/bin/env python3
"""Task 2's module."""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension
    four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.

    Returns:
        float: Total runtime in seconds.
    """
    start = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end = time.time()
    return end - start
