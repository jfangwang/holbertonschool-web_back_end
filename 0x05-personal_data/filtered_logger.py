#!/usr/bin/env python3
"""Regex"""
from typing import List
import re

def filter_datum(fields: List[str], redaction, message: str, separator: str):
    """returns the log message obfuscated"""
    for entry in fields:
        message = re.sub(f"{entry}=.+?{separator}", f"{entry}={redaction}{separator}", message)
    return message
