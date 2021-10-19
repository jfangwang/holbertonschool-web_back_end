#! /usr/bin/env python3
"""Basic annotation: basic async syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine that takes in an integer argument"""
    rand_num = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return rand_num
