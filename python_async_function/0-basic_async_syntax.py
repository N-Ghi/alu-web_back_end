#!/usr/bin/env python3
"""Module that provides an asynchronous coroutine to wait a random time."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Documentation string for wait_random function.
    """
    delay: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
