#! /usr/bin/env python3

from ast import literal_eval
import itertools as it
import functools as ft
import more_itertools as mit
import regex as re
import numpy as np
import sympy as syp
import scipy as scp
import urllib3 as ul
import requests as rq
import bs4 as bs
import dateutil.parser as dp

from textwrap import dedent, indent
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2015, day=8))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (r'""', 2),
        (r'"abc"', 2),
        (r'"aaa\"aaa"', 3),
        (r'"\x27"', 5),
    ],
    "B": [
        (r'""', 4),
        (r'"abc"', 4),
        (r'"aaa\"aaa"', 6),
        (r'"\x27"', 5),
    ],
}


def A(input: str) -> int:
    total = 0
    for line in input.splitlines():
        literal = literal_eval(line)
        total += len(line) - len(literal)

    return total


def B(input: str) -> int:
    total = 0
    for line in input.splitlines():
        encoded = '"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'
        total += len(encoded) - len(line)

    return total


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=8, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=8, year=2015)
