#!/usr/bin/env python3
"""Module that concurrently runs task_wait_random n times."""

import asyncio
from typing import List
from heapq import heappush, heappop

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Documenaton string for task_wait_n function.
    """
    heap: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        heappush(heap, delay)

    return [heappop(heap) for _ in range(len(heap))]
