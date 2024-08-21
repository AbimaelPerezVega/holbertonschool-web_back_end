#!/usr/bin/env python3
"""This module contains the async_generator coroutine."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """Yields a random number between 0 and 10 asynchronously after waiting 1 second, 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
