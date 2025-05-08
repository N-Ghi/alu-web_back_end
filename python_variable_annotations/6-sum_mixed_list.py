#!/usr/bin/env python3
"""Compute the sum of a mixed list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Elements in mxd_lst, which contains both integers and floats."""
    return float(sum(mxd_lst))
