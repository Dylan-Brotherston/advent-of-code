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


puzzle_data: str = clean(get_data(year=2015, day=10))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def A(input: str) -> int:
    def look_and_say(s: str) -> list[str]:
        return ["".join(g) for _, g in it.groupby(s)]
    for _ in range(40):
        output = ""
        runs = look_and_say(input)
        for run in runs:
            output += str(len(run)) + run[0]

        input = output
    return len(input)


def B(input: str) -> int:
    def look_and_say(s: str) -> list[str]:
        return ["".join(g) for _, g in it.groupby(s)]
    for _ in range(50):
        output = ""
        runs = look_and_say(input)
        for run in runs:
            output += str(len(run)) + run[0]

        input = output
    return len(input)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=10, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=10, year=2015)
