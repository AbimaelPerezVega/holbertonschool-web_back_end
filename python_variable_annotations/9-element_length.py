#!/usr/bin/env python3
"""
This module provides a type-annotated function
that returns a list of tuples with elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
