#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
<<<<<<< HEAD
from typing import List
=======
from typing import List, Dict
>>>>>>> 4b415e05279f8f66052b1c658beb3afae118e333


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

<<<<<<< HEAD
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert str(index).isnumeric() and type(page_size) is int
        assert index >= 0 and index < len(self.indexed_dataset())
        output = []
        next_index = index + page_size
        return {'index': index,
                'next_index': next_index,
                'page_size': page_size,
                'data': output
                }
=======
    def get_hyper_index(self, index: int = None, page_size: int = 10) ->\
            Dict[str, any]:
        """return a dictionary containing index, next index,
        page size, and data"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        assert index < len(self.indexed_dataset())
        data = []
        next_idx = index + page_size
        for a in range(index, index + page_size, 1):
            if self.indexed_dataset().get(a):
                data.append(self.indexed_dataset().get(a))

        return {
            'index': index,
            'next_index': next_idx,
            'page_size': page_size,
            'data': data
        }
>>>>>>> 4b415e05279f8f66052b1c658beb3afae118e333
