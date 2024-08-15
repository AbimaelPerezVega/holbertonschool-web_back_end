#!/usr/bin/env python3
"""
This module provides a function to measure
the runtime of an asynchronous function.
"""

import time
import asyncio
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time
    for wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time for each wait_random.

    Returns:
        float: The average time per wait_random call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
