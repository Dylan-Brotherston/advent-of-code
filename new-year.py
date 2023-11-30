#! /usr/bin/env python3

from sys import argv, exit
from os import mkdir, chmod, symlink
from os.path import exists
from string import Template

if len(argv) != 2:
    print(f"Usage: {argv[1]} <year>")
    exit(1)

try:
    year = int(argv[1])
except ValueError:
    print(f"Invalid year: {argv[1]}")
    exit(1)

if not exists("template.py"):
    print("template.py not found")
    exit(1)

template = open("template.py").read()

if not exists("share.py"):
    print("share.py not found")
    exit(1)

if not exists(f"year-{year}"):
    print(f"Creating directory for year {year}")
    mkdir(f"year-{year}")

T = Template(template)

for i in range(1, 26):
    if not exists(f"year-{year}/day-{i}"):
        print(f"Creating day {year}/{i}")

        mkdir(f"year-{year}/day-{i}")
        open(f"year-{year}/day-{i}/solve.py", "w").write(
            T.substitute({"DAY": i, "YEAR": year})
        )
        chmod(f"year-{year}/day-{i}/solve.py", 0o755)
        symlink("../../share.py", f"year-{year}/day-{i}/share.py")
    else:
        print(f"Day {year}/{i} already exists")
