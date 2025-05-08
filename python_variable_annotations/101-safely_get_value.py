#!/usr/bin/env python3
"""This module provides a function to safely get a value from a dictionary."""

from typing import TypeVar, Optional, Mapping, Any

T = TypeVar('T')

def safely_get_value(dct: Mapping[str, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """Return the value associated with key from the dictionary, or default if key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
