#!/usr/bin/python3
"""log parsing"""
import sys


def display_metrics(total_size, status_code):
    """Function that prints the metrics"""
    print("File size:", total_size)
    for key, value in sorted(status_code.items()):
        if value > 0:
            print(f"{key}: {value}")


def log_parse() -> None:
    """A function that reads stdin line by line and computes metrics"""
    while True:
        line_count = 0
        total_f_size = 0
        status_code = {
            '200': 0, '301': 0, '400': 0, '401': 0,
            '403': 0, '404': 0, '405': 0, '500': 0
        }
        try:
            for line in sys.stdin:
                args = line.split()
                if len(args) < 7:
                    continue  # Skip lines that don't match the format

                status = args[-2]
                file_size = args[-1]
                total_f_size += int(file_size)

                if status in status_code:
                    status_code[status] += 1

                line_count += 1

                if line_count % 10 == 0:
                    display_metrics(total_f_size, status_code)

        except KeyboardInterrupt:
            display_metrics(total_f_size, status_code)
            raise
        else:
            display_metrics(total_f_size, status_code)


if __name__ == '__main__':
    log_parse()
