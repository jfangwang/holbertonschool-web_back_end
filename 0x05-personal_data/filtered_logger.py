#!/usr/bin/env python3
"""Regex"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


def filter_datum(fields: List[str],
                 redaction, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for entry in fields:
        message = re.sub(f'{entry}=.+?{separator}',
                         f'{entry}={redaction}{separator}', message)
    return message
