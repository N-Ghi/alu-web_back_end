#!/usr/bin/env python3
"""Create a tuple with a string and the square of a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """String k and the square of v (int or float) as a float."""
    return (k, float(v ** 2))
