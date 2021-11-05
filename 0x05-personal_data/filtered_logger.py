#!/usr/bin/env python3
"""Regex"""
from typing import List


def filter_datum(fields: List[str], redaction, message: str, separator: str):
    """returns the log message obfuscated"""
    return "{}".format(fields)
