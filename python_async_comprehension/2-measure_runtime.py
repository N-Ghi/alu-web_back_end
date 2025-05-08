#!/usr/bin/env python3
"""Runtime measurement module.
Measures the execution time of running async_comprehension
four times in parallel.
"""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measures and returns the total execution time for running
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
