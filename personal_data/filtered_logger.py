#!/usr/bin/env python3
"""
Module for obfuscating log data.
"""

import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscate specified fields in a log message.
    """
    pattern = ''.join(
        [f'({re.escape(field)}=)[^{re.escape(separator)}]*({re.escape(separator)})'
        for field in fields]
    )
    return re.sub(pattern, rf'\1{redaction}\2', message)
