#!/usr/bin/env python3
"""
This module provides a type-annotated function
for summing a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        The list of integers and floats to sum.

    Returns:
        float: The sum of the list of integers and floats.
    """
    return float(sum(mxd_lst))
