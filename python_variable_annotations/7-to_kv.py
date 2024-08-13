#!/usr/bin/env python3
"""
This module provides a type-annotated function
for creating a tuple with a string and the square of a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and the square of a number.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to square and include in the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first
        element is the string and the second element is
        the square of the number.
    """
    return (k, float(v ** 2))
