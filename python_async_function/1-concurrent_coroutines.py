#!/usr/bin/env python3
"""
This module provides an asynchronous
coroutine that spawns wait_random n times
and returns the list of delays.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the
    specified max_delay and return the list of all delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time for each wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
