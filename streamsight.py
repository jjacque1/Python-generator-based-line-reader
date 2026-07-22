"""
streamsight.py
A small CLI tool that streams and filters text files using generators.
"""

import sys


def read_lines(path):
    """Generator that yields one stripped line at a time from a file."""
    with open(path) as f:
        for line in f:
            yield line.strip()


def filter_lines(path, keyword):
    """Generator that yields only lines containing `keyword`."""
    for line in read_lines(path):
        if keyword in line:
            yield line


def count_lines(path):
    """Uses read_lines() without loading the whole file into memory."""
    count = 0
    for _ in read_lines(path):
        count += 1
    return count


if __name__ == "__main__":
    filepath = sys.argv[1]

    if len(sys.argv) > 2:
        keyword = sys.argv[2]
        print(f"Lines containing '{keyword}':")
        for line in filter_lines(filepath, keyword):
            print(f"  {line}")
    else:
        print(f"Lines: {count_lines(filepath)}")

