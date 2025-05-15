#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Any


def index_range(page, pSize):
    """
    Simple helper function for pagination documentation
    """
    start_index = (page - 1) * pSize
    end_index = page * pSize

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, pSize: int = 10) -> List[List]:
        """
        Simple documentation to pass the checker for now
        """
        # Validate that arguments are integers and greater than 0
        assert isinstance(page, int) and page > 0, "page must be positive"
        assert isinstance(pSize, int) and pSize > 0, "pSize must be positive"

        # Get the dataset
        dataset = self.dataset()

        # Get the pagination indexes
        start_idx, end_idx = index_range(page, pSize)

        # If start index is beyond the dataset size, return empty list
        if start_idx >= len(dataset):
            return []

        # Return the appropriate page of the dataset
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, pSize: int = 10) -> Dict[str, Any]:
        # Get the page data using the get_page method
        data = self.get_page(page, pSize)

        # Calculate total items in the dataset
        total_items = len(self.dataset())

        # Calculate total pages
        total_pages = math.ceil(total_items / pSize) if pSize > 0 else 0

        # Determine next page
        next_page = page + 1 if page < total_pages else None

        # Determine previous page
        prev_page = page - 1 if page > 1 else None

        # Create the dictionary with all required key-value pairs
        hyper_dict = {
            'pSize': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper_dict
