#!?usr/bin/env python3
"""Helper function to compute pagination index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """compute page size in tuple"""
    start_index = (page - 1) * page_size
    stop_index = page * page_size
    return (start_index, stop_index)
