#!/usr/bin/env python3
"""
Module for obfuscating log data
"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate specified fields in a log message"""
    pattern = ''.join([f'({field}=)[^{separator}]*({separator})' for field in fields])
    return re.sub(pattern, f'\\1{redaction}\\2', message)
