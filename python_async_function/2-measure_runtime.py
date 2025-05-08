#!/usr/bin/env python3
"""Module for measuring the average execution time of wait_n."""

import time
import asyncio
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Documentation string for measure_time function.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time / n
