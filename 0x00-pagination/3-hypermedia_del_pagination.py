#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        """Return a page of the dataset (hypermedia)
        with deletion-resilient pagination."""
        # Assert that the index is within the valid range
        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)

        # Generate the list of data starting from the given index
        data = []
        current_index = index
        count = 0

        while count < page_size and current_index < dataset_size:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
