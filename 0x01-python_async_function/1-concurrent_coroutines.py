#!/usr/bin/env python3
"""Task 1's solution."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute 'n' instances of wait_random
    concurrently with a maximum delay of 'max_delay'.

    Args:
        n (int): Number of concurrent executions.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: Delays of each execution,
        sorted in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
