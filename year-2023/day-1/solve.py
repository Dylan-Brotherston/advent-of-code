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


puzzle_data: str = clean(get_data(year=2023, day=1))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
        (
            clean(
                """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
            ),
            142,
        ),
    ],
    "B": [
        (
            clean(
                """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
            ),
            281,
        ),
    ],
}


def A(input: str) -> int:
    n = []
    for line in input.splitlines():
        numbers = re.findall(r"\d", line)
        num = int(numbers[0] + numbers[-1])
        n.append(num)

    return sum(n)


def B(input: str) -> int:
    n = []
    for line in input.splitlines():
        numbers = []
        while line:
            if line.startswith("one") or line.startswith("1"):
                numbers.append("1")
            if line.startswith("two") or line.startswith("2"):
                numbers.append("2")
            if line.startswith("three") or line.startswith("3"):
                numbers.append("3")
            if line.startswith("four") or line.startswith("4"):
                numbers.append("4")
            if line.startswith("five") or line.startswith("5"):
                numbers.append("5")
            if line.startswith("six") or line.startswith("6"):
                numbers.append("6")
            if line.startswith("seven") or line.startswith("7"):
                numbers.append("7")
            if line.startswith("eight") or line.startswith("8"):
                numbers.append("8")
            if line.startswith("nine") or line.startswith("9"):
                numbers.append("9")
            line = line[1:]
        numbers = int(numbers[0] + numbers[-1])
        n.append(numbers)

    return sum(n)


for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"{recived} != {solution}"
submit(A(puzzle_data), part="a", day=1, year=2023)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"{recived} != {solution}"
submit(B(puzzle_data), part="b", day=1, year=2023)
