#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from aocd import get_data, submit # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2015, day=2))
sample_data: str = clean("""
2x3x4
1x1x10
""")


def A(input: str) -> int:
    total = 0
    for line in by_lines(input):
        l, w, h = map(int, line.split('x'))
        sides = [l*w, w*h, h*l]
        total += 2*sum(sides) + min(sides)
    return total


def B(input: str) -> int:
    total = 0
    for line in by_lines(input):
        l, w, h = map(int, line.split('x'))
        sides = [l+w, w+h, h+l]
        total += 2*min(sides) + l*w*h
    return total


assert A(sample_data) == 101, A(sample_data)
submit(A(data), part="a", day=2, year=2015)

assert B(sample_data) == 48, B(sample_data)
submit(B(data), part="b", day=2, year=2015)
