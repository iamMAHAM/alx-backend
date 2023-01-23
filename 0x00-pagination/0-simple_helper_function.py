#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        tuple with the range start and end size page
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
