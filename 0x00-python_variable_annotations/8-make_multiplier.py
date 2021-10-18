#!/usr/bin/env python3
"""Basic annotation: make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(num: float):
        return num * multiplier
    return multiply
