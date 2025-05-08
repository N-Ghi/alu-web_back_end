#!/usr/bin/env python3
"""Module that concurrently runs multiple wait_random coroutines."""

import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Documentation string for wait_n function.
    """
    heap: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        heappush(heap, delay)

    return [heappop(heap) for _ in range(len(heap))]
