#!/usr/bin/env python3
"""
Module for obfuscating log data
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message"""
    pattern = ''.join([f'({field}=)[^{separator}]*({separator})' for field in fields])
    return re.sub(pattern, f'\\1{redaction}\\2', message)
