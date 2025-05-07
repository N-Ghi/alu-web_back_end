#!/usr/bin/env python3
"""This module provides a function to safely return the first element of a list, or None."""

from typing import Any, Optional, List

def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """Return the first element of the list if it exists, otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None
