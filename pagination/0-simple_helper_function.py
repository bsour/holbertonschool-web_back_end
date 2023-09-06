#!/usr/bin/env python3
'''
function named index_range that takes two integer arguments
page and page_size
'''


def index_range(page, page_size):
    '''
    Get starting and an end index
    Args:
         page: page number
         page_size: size of the page

    Return:
           List of particular pagination parameters
    '''
    start_index = (page_size * (page - 1))
    last_index = (page * page_size)
    result = (start_index, last_index)

    return result
