#!/usr/bin/env python3
"""Basic annotation: concurrent coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values).
    The list of the delays should be in ascending order without
    using sort() because of concurrency."""
    delay_list: List[float] = []
    sorted_list: List[float] = []

    for index in range(0, n):
        delay_list.append(wait_random(max_delay))
    for item in asyncio.as_completed(delay_list):
        """Waits until item is complete and stores into sorted list"""
        result = await item
        sorted_list.append(result)
    return sorted_list
