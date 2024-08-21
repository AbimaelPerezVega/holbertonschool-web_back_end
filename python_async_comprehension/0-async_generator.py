#!/usr/bin/env python3
"""
This module contains the async_generator coroutine.

The async_generator coroutine generates 10 random floating-point numbers 
between 0 and 10, with a 1-second asynchronous delay between each number.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Asynchronously generates 10 random numbers.

    This coroutine yields 10 random floating-point numbers between 0 and 10.
    Each number is generated after an asynchronous delay of 1 second.

    Returns:
        Generator[float, None, None]: A generator yielding 10 random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
