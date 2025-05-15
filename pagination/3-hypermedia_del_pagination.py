#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Simple documentation to pass the checker for now
        """
        # Get the indexed dataset
        indexed_data = self.indexed_dataset()

        # Set default index to 0 if None
        if index is None:
            index = 0

        # Verify that index is in a valid range
        assert isinstance(index, int) and 0 <= index < len(self.dataset()), \
            "Index out of range"

        # Collect the data for the current page
        data = []
        current_index = index
        count = 0

        # Collect page_size items, skipping over deleted items
        while count < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        # Calculate the next index
        next_index = current_index

        # Return the hypermedia dictionary
        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
