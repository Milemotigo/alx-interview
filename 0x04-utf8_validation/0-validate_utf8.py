#!/usr/bin/python3
"""
 method that determines if a given data
 set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding,
    else return False
    """
    byte_reamining = 0
    for byte in data:
        if byte_reamining == 0:
            if byte >> 7 == 0b0:
                byte_reamining == 0
            elif byte >> 5 == 0b110:
                byte_reamining == 1
            elif byte >> 4 == 0b1110:
                byte_reamining == 2
            elif byte >> 3 == 0b11110:
                byte_reamining == 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            byte_reamining -= 1
    return byte_reamining == 0
