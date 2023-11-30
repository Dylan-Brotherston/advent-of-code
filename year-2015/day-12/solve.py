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
import json

from textwrap import dedent, indent
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2015, day=12))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (clean("[1,2,3]"), 6),
        (clean('{"a":2,"b":4}'), 6),
        (clean('[[[3]]]'), 3),
        (clean('{"a":{"b":4},"c":-1}'), 3),
        (clean('{"a":[-1,1]}'), 0),
        (clean('[-1,{"a":1}]'), 0),
        (clean('[]'), 0),
        (clean('{}'), 0),
    ],
    "B": [
        (clean("[1,2,3]"), 6),
        (clean('[1,{"c":"red","b":2},3]'), 4),
        (clean('{"d":"red","e":[1,2,3,4],"f":5}'), 0),
        (clean('[1,"red",5]'), 6),
    ],
}


def A(input: str) -> int:
    data = json.loads(input)
    def sum_numbers(data: dict | list | int) -> int:
        if isinstance(data, int):
            return data
        if isinstance(data, list):
            return sum(map(sum_numbers, data))
        if isinstance(data, dict):
            return sum(map(sum_numbers, list(data.values())))
        return 0
    return sum_numbers(data)


def B(input: str) -> int:
    data = json.loads(input)
    def sum_numbers(data: dict | list | int) -> int:
        if isinstance(data, int):
            return data
        if isinstance(data, list):
            return sum(map(sum_numbers, data))
        if isinstance(data, dict):
            if "red" in data.values():
                return 0
            return sum(map(sum_numbers, list(data.values())))
        return 0
    return sum_numbers(data)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=12, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=12, year=2015)
