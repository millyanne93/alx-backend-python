#!/usr/bin/env python3
"""Task 3."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio.Task to execute wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        asyncio.Task: A task to execute wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
