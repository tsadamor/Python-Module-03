#! /usr/bin/python3.12

import sys

argv = sys.argv
argc = len(argv)

print("=== Command Quest ===")
print(f"Program name: {argv[0]}")
if argc == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {argc - 1}")
    for i in range(1, argc):
        print(f"Argument {i}: {argv[i]}")
print(f"Total arguments: {argc}\n")
