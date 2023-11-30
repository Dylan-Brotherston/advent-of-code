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


puzzle_data: str = clean(get_data(year=2015, day=13))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("""
            Alice would gain 54 happiness units by sitting next to Bob.
            Alice would lose 79 happiness units by sitting next to Carol.
            Alice would lose 2 happiness units by sitting next to David.
            Bob would gain 83 happiness units by sitting next to Alice.
            Bob would lose 7 happiness units by sitting next to Carol.
            Bob would lose 63 happiness units by sitting next to David.
            Carol would lose 62 happiness units by sitting next to Alice.
            Carol would gain 60 happiness units by sitting next to Bob.
            Carol would gain 55 happiness units by sitting next to David.
            David would gain 46 happiness units by sitting next to Alice.
            David would lose 7 happiness units by sitting next to Bob.
            David would gain 41 happiness units by sitting next to Carol.
        """), 330),
    ],
    "B": [
    ],
}


def A(input: str) -> int:
    happiness = {}
    for line in input.splitlines():
        a, _, sign, amount, _, _, _, _, _, _, b = line.split()
        happiness[(a, b[:-1])] = int(amount) * (1 if sign == "gain" else -1)

    best = None
    for order in it.permutations(set(a for a, _ in happiness.keys())):
        total = 0
        for a, b in mit.windowed(order + (order[0],), 2):
            total += happiness[(a, b)] + happiness[(b, a)]
        best = max(best, total) if best else total

    return best

def B(input: str) -> int:
    happiness = defaultdict(lambda: 0)
    for line in input.splitlines():
        a, _, sign, amount, _, _, _, _, _, _, b = line.split()
        happiness[(a, b[:-1])] = int(amount) * (1 if sign == "gain" else -1)

    best = None
    for order in it.permutations(set(a for a, _ in happiness.keys()) | {"me"}):
        total = 0
        for a, b in mit.windowed(order + (order[0],), 2):
            total += happiness[(a, b)] + happiness[(b, a)]
        best = max(best, total) if best else total

    return best


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=13, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=13, year=2015)
