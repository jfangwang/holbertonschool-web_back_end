#!/usr/bin/env python3
"""Basic annotation: async comprehension"""
import asyncio
import random
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """The coroutine will loop 10 times, each time
    asynchronously wait 1 second, then yield a random
    number between 0 and 10. Use the random module."""
    random_num_list = [i async for i in async_generator()]
    return random_num_list
