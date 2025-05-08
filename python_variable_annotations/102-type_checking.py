#!/usr/bin/env python3
"""Function to zoom an array by a specified factor."""

from typing import List, Any, Tuple


def zoom_array(lst: Tuple[Any], factor: int = 2) -> List:
    """Return a list that repeats each element of lst factor times."""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
