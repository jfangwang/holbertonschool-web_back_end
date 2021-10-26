#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """return a tuple of size two containing a start
    index and an end index corresponding to the range"""
    if page and page_size:
        start = (page - 1) * page_size
        end = start + page_size
        return(start, end)
