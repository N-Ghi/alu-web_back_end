#!/usr/bin/env python3
"""Safely return the first element of a list, or None."""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return list if it exists, otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None
