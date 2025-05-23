#!/usr/bin/env python3
"""Function returning an asyncio Task for wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Documenaton string for task_wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))
