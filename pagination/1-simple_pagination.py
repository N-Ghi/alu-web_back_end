#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Simple helper function for pagination documentation
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        # Validate that arguments are integers and greater than 0
        assert isinstance(page, int) and page > 0,"page must be positive"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be positive"

        # Get the dataset
        dataset = self.dataset()

        # Get the pagination indexes
        start_idx, end_idx = index_range(page, page_size)

        # If start index is beyond the dataset size, return empty list
        if start_idx >= len(dataset):
            return []

        # Return the appropriate page of the dataset
        return dataset[start_idx:end_idx]
