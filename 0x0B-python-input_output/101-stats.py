#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics:"""
import sys
import signal

def print_stats():
    """script that reads stdin line by line and computes metrics:"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """script that reads stdin line by line and computes metrics:"""
    print_stats()
    sys.exit(0)

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0

signal.signal(signal.SIGINT, signal_handler)

for i, line in enumerate(sys.stdin, 1):
    try:
        data = line.split()
        size = int(data[-1])
        status_code = data[-2]
        total_size += size
        if status_code in status_codes:
            status_codes[status_code] += 1
    except:
        pass

    if i % 10 == 0:
        print_stats()
print_stats()

