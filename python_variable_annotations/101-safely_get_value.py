#!/usr/bin/env python3
"""This module provides a function to safely get a value from a dictionary."""

from typing import Dict, TypeVar, Optional

T = TypeVar('T')

def safely_get_value(dct: Dict[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    """Return the value associated with key from the dictionary, or default if key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
