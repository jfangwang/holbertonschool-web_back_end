#!/usr/bin/env python3
"""Basic annotation: type checking"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Use mypy to validate the following piece of
    code and apply any necessary changes."""
    zoomed_in: List = [
        ele for ele in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
