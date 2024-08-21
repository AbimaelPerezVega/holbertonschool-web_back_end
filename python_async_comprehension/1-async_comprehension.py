#!/usr/bin/env python3
"""This module contains the async_comprehension coroutine."""

import asyncio
from typing import List

# Importing the async_generator function
task_0_function = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator
    using an async comprehension."""

    return [i async for i in task_0_function()]
