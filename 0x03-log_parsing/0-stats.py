#!/usr/bin/env python3
"""Reads stdin line by line and computes metrics"""

import sys
import re
import signal

total_size = 0
status_codes = {}
line_count = 0

def print_statistics():
    """Print the required statistics"""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle CTRL+C by printing statistics and exiting"""
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Regular expression pattern for the log line format
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

try:
    for line in sys.stdin:
        match = re.match(pattern, line.strip())
        if match:
            # Extract status code and file size
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Update metrics
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
except Exception as e:
    print(f"Error processing input: {e}", file=sys.stderr)
    sys.exit(1)
