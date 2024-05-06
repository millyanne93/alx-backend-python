#!/usr/bin/env python3
"""Task 4's module."""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times.

    Args:
        n (int): Number of concurrent executions.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of all the delays
        (float values) in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
