#!/usr/bin/env python3
""" Simple pagiantion """
import typing
from typing import Tuple, List
import csv
import math


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
        """
        Retrieves a specific page of data from
        the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range = index_range(page, page_size)

        if (len(self.dataset()) < range[1]):
            return []

        return self.__dataset[range[0]: range[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple representing the start and end indices
    for a given page and page size.
    """
    end = page * page_size
    start = end - page_size
    return tuple([start, end])
