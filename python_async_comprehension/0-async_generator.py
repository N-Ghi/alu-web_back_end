#!/usr/bin/env python3
"""Async generator module.
Generates 10 random floats between 0 and 10, each after a 1-second delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """Asynchronously yields 10 random floats between 0 and 10 with a delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
