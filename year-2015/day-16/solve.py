#! /usr/bin/env python3

import sys, os
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


puzzle_data: str = clean(get_data(year=2015, day=16))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def A(input: str) -> int:
    aunts = []
    for line in input.splitlines():
        m = re.fullmatch(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)
        aunts.append({m[2]: int(m[3]), m[4]: int(m[5]), m[6]: int(m[7])})

    for i, aunt in enumerate(aunts):
        for k, v in aunt.items():
            if target[k] != v:
                break
        else:
            return i + 1

    return None


def B(input: str) -> int:
    aunts = []
    for line in input.splitlines():
        m = re.fullmatch(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)
        aunts.append({m[2]: int(m[3]), m[4]: int(m[5]), m[6]: int(m[7])})

    for i, aunt in enumerate(aunts):
        for k, v in aunt.items():
            if k in ("cats", "trees"):
                if target[k] >= v:
                    break
            elif k in ("pomeranians", "goldfish"):
                if target[k] <= v:
                    break
            elif target[k] != v:
                break
        else:
            return i + 1


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=16, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=16, year=2015)
