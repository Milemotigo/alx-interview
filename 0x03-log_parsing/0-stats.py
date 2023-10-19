import sys
import re
from collections import defaultdict

# Initialize variables to store metrics
total_size = 0
status_counts = defaultdict(int)

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        # Use a regular expression to parse the line
        match = re.match(r'(\S+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_size += file_size
            status_counts[status_code] += 1

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    pass

# Print final metrics after processing all lines
print(f"Total file size: {total_size}")
for code in sorted(status_counts.keys()):
    print(f"{code}: {status_counts[code]}")