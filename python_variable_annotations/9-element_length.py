#!/usr/bin/env python3
"""Return a list of tuples with elements and their lengths."""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Each tuple contains a sequence and its length."""
    return [(i, len(i)) for i in lst]
