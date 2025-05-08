#!/usr/bin/env python3
"""Function to create a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
