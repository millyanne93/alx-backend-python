#!/usr/bin/env python3
"""Task 0 solution."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that generates random
    numbers asynchronously.

    This coroutine loops 10 times, each time
    asynchronously waiting for 1 second,
    then yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
