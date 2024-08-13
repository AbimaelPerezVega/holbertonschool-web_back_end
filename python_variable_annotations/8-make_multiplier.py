#!/usr/bin/env python3
"""
This module provides a type-annotated function
that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float):
        The multiplier value to use in the created function.

    Returns:
        Callable[[float], float]:
        A function that multiplies a float by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
