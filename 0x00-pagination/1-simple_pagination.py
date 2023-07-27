#!/usr/bin/env python3
"""a simple pagination algorithm"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple:
        """compute page size in tuple"""
        start_index = (page - 1) * page_size
        stop_index = page * page_size
        return (start_index, stop_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """fetch page using simple pagination"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, stop_index = self.index_range(page, page_size)
        if len(self.dataset()) < start_index \
                or len(self.dataset()) < stop_index:
            return []
        return [self.dataset()[i] for i in range(start_index, stop_index)]
