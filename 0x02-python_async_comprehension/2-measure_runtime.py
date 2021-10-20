#!/usr/bin/env python3
"""Basic annotation: async comprehension"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime by using asyncio.gather"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
