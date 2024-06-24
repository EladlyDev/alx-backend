#!/usr/bin/env python3
""" Simple helper function """
import typing
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple representing the start and end indices
    for a given page and page size.
    """
    end = page * page_size
    start = end - page_size
    return tuple([start, end])
