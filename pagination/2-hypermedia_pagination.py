#!/usr/bin/env python3
'''
Implement a get_hyper method that takes the same
arguments (and defaults) as get_page and returns
a dictionary containing the following key-value pairs:
'''
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Get starting and an end index
    Args:
         page: page number
         page_size: size of the page

    Return:
           List of particular pagination parameters
    """
    start_index = (page_size * (page - 1))
    last_index = (page * page_size)
    result = (start_index, last_index)

    return result


class Server:
    '''
    Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data based on page number and page size.
        """
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve hypermedia information for a specific page.
        """
        dataset_page = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hypermedia = {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hypermedia
