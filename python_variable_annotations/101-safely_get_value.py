#!/usr/bin/env python3
"""Safely get a value from a dictionary."""

from typing import TypeVar, Optional, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T, None]:
    """Return key from the dictionary, or default if key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
