#!/usr/bin/env python3
"""
This module provides a type-annotated function for summing a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
