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
    first_index = (page - 1) * page_size
    last_index = page * page_size - 1

    return (first_index, last_index)
