#!/usr/bin/env python3
"""
This module provides a type-annotated function
for returning the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float.

    Args:
        n (float): The float to floor.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)
