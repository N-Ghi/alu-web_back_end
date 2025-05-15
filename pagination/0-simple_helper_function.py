#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page, page_size):
    """
    Simple helper function for pagination documentation
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
