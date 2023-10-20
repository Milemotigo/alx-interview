#!/usr/bin/python3
"""log parsing"""
import sys
import re

def match(x: str) -> bool:
    """Checks for input match"""
    ip_match = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
    date_match = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
    stats_match = r'"GET /projects/260 HTTP/1\.1" \d{3} \d+'
    pattern = ip_match + date_match + stats_match
    return True if re.match(pattern, x) else False

def log_parse() -> None:
    """ A function that reads stdin line by line and computes metrics """
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    
    line_count = 0

    try:
        for line in sys.stdin:
            if match(line):
                a, b, c, d, e, f, g, status_code, f_size = line.split()
                total_size += int(f_size)
                if status_code in status_codes:
                    status_codes[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print(f'File size: {total_size}')
                    for key, val in status_codes.items():
                        if val > 0:
                            print(f"{key}: {val}")

    except KeyboardInterrupt:
        print(f'File size: {total_size}')
        for key, val in status_codes.items():
            if val > 0:
                print(f"{key}: {val}")
        exit(1)

if __name__ == '__main__':
    log_parse()