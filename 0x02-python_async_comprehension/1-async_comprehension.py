#!/usr/bin/env python3
"""Task 1 solution
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    using an async comprehension over async_generator.

    Returns:
        List[float]: List of 10 random numbers.
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
