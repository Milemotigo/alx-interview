#!/usr/bin/env python3
"""0. Regex-ing"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Filters a log message by obfuscating certain fields.

    Args:
        fields: A list of strings representing all fields to obfuscate.
        redaction: A string representing by what the field will be obfuscated.
        message: A string representing the log line.
        separator: A string representing by which character is separating
        all fields in the log line (message).

    Returns:
        A string representing the obfuscated log line.
    """
    regex = '|'.join([re.escape(field) for field in fields])
    return re.sub(f'({regex})=[^{separator}]*', f'\\1={redaction}', message)
