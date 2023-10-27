#!/usr/bin/python3
"""
module: 0-validate_utf8.py
"""


def validUTF8(data):
    """
    method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    if len(data) == 1:
        for i in data:
            if i > 127:
                return False
            else:
                return True
    elif len(data) > 1:
        if len(data) == 2 and data[0] > 223:
            return False

        else:
            new_data = data[1:]
            for i in range(len(new_data)):
                if new_data[i] > 191:
                    return False
    return True