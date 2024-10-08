#!/usr/bin/env python3
"""
This module provides an asynchronous
coroutine that waits for a random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between
    0 and max_delay seconds and return the delay.

    Args:
        max_delay (int, optional):
        The maximum delay time in seconds. Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
