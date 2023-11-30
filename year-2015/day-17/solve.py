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


puzzle_data: str = clean(get_data(year=2015, day=17))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def find_combinations(containers, target):
    for i in range(len(containers)):
        for combination in it.combinations(containers, i):
            if sum(combination) == target:
                yield combination


def A(input: str) -> int:
    containers = [int(line) for line in input.splitlines()]
    return len(list(find_combinations(containers, 150)))



def B(input: str) -> int:
    containers = [int(line) for line in input.splitlines()]
    combinations = list(map(len, find_combinations(containers, 150)))
    return len(list(filter(lambda x: x == min(combinations), combinations)))



for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=17, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=17, year=2015)
