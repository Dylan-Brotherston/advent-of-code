#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from textwrap import indent

from aocd import get_data, submit # type: ignore

from share import *


puzzle_data: str = clean(get_data(year=2015, day=1))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
    "B": [
        (")", 1),
        ("()())", 5),
    ]
}


def A(input: str) -> int:
    """
    Santa is trying to deliver presents in a large apartment building,
    but he can't find the right floor - the directions he got are a little confusing.
    He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor,
    and a closing parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep;
    he will never find the top or bottom floors.

    To what floor do the instructions take Santa?
    """
    from collections import Counter

    C = Counter(input)

    return C['('] - C[')']


def B(input: str) -> int:
    """
    Now, given the same instructions,
    find the position of the first character that causes him to enter the basement (floor -1).
    The first character in the instructions has position 1, the second character has position 2, and so on.

    What is the position of the character that causes Santa to first enter the basement?
    """
    level = 0

    for i, c in enumerate(input, 1):
        if c == '(':
            level += 1
        if c == ')':
            level -= 1
        if level < 0:
            return i

for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=1, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=1, year=2015)
