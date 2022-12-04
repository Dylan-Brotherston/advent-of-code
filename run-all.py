#! /usr/bin/env python3

from sys import argv, exit
from os.path import exists
from subprocess import run

if len(argv) != 2:
    print(f"Usage: {argv[1]} <year>")
    exit(1)

try:
    year = int(argv[1])
except ValueError:
    print(f"Invalid year: {argv[1]}")
    exit(1)

for day in range(1, 26):
    if not exists(f"year-{year}/day-{day}/solve.py"):
        continue

    print(f"Running day {year}/{day}")
    run(["./year-{year}/day-{day}/solve.py"], shell=True)
