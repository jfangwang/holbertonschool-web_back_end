#!/usr/bin/env python3
"""Basic annotation: tasks"""
import asyncio
from typing import List
task_wait_r = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is
    being called."""
    delay_list: List[float] = []
    sorted_list: List[float] = []

    for index in range(0, n):
        delay_list.append(task_wait_r(max_delay))
    for item in asyncio.as_completed(delay_list):
        """Waits until item is complete and stores into sorted list"""
        sorted_list.append(await item)
    return sorted_list
