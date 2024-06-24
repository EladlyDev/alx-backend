#!/usr/bin/env python3
""" Hypermedia pagination """
import typing
from typing import Tuple, List, Dict
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves a dictionary containing
        hypermedia pagination information.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_pages = len(self.dataset())
        range = index_range(page, page_size)
        data = self.get_page(page, page_size)
        next_page = None if range[1] > total_pages else page + 1
        prev_page = None if range[0] < 1 else page - 1

        return dict(page_size=page_size, page=page,
                    data=data, next_page=next_page,
                    prev_page=prev_page, total_pages=total_pages)


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple representing the start and end indices
    for a given page and page size.
    """
    end = page * page_size
    start = end - page_size
    return tuple([start, end])
