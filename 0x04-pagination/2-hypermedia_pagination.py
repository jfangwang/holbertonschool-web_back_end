#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """return a tuple of size two containing a start
    index and an end index corresponding to the range"""
    if page and page_size:
        start = (page - 1) * page_size
        end = start + page_size
        return(start, end)


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        output = []
        if start >= len(self.dataset()):
            return []
        output = self.dataset()
        return output[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_count = math.ceil((len(self.dataset()) / page_size))
        if page + 1 < page_count:
            next_page = page + 1
        else:
            next_page = None
        if page - 1 > 1:
            prev_page = page - 1
        else:
            prev_page = None
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': page_count
                }
