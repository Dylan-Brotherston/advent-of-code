#! /usr/bin/env python3

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


puzzle_data: str = clean(get_data(year=2015, day=11))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def increment_string(s: str) -> str:
    if s == "":
        return "a"
    if s[-1] == "z":
        return increment_string(s[:-1]) + "a"
    return s[:-1] + chr(ord(s[-1]) + 1)

def is_valid(input: str) -> bool:
    found = False
    for a, b, c in mit.windowed(input, 3):
        if ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c):
            found = True
            break
    if not found:
        return False

    if "i" in input or "o" in input or "l" in input:
        return False

    if len(re.findall(r"(.)\1", input)) < 2:
        return False

    return True


def A(input: str) -> int:
    input = increment_string(input)
    while not is_valid(input):
        input = increment_string(input)
    return input


def B(input: str) -> int:
    input = increment_string(input)
    while not is_valid(input):
        input = increment_string(input)
    input = increment_string(input)
    while not is_valid(input):
        input = increment_string(input)
    return input


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=11, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=11, year=2015)
