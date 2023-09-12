#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics:"""


import sys

total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 7:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {:d}".format(total_file_size))
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print("{:d}: {:d}".format(code, count))

except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully

finally:
    print("File size: {:d}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{:d}: {:d}".format(code, count))
