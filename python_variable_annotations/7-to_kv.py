#!/usr/bin/env python3
"""This module provides a function to create a tuple with a string and the square of a number."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v (int or float) as a float."""
    return (k, float(v ** 2))
