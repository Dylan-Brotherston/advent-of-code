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


data: str = clean(get_data(year=2015, day=3))
sample_data: str = clean("""
^v^v^v^v^v
""")


def A(input: str) -> int:
    position = (0, 0)
    visited = {position,}
    for char in list(input):
        match char:
            case '^':
                position = (position[0], position[1] + 1)
            case 'v':
                position = (position[0], position[1] - 1)
            case '>':
                position = (position[0] + 1, position[1])
            case '<':
                position = (position[0] - 1, position[1])
        visited.add(position)
    return len(visited)


def B(input: str) -> int:
    positions = [(0, 0), (0, 0)]
    visited = {positions[0],}
    for i, char in enumerate(input):
        match char:
            case '^':
                positions[i%2] = (positions[i%2][0], positions[i%2][1] + 1)
            case 'v':
                positions[i%2] = (positions[i%2][0], positions[i%2][1] - 1)
            case '>':
                positions[i%2] = (positions[i%2][0] + 1, positions[i%2][1])
            case '<':
                positions[i%2] = (positions[i%2][0] - 1, positions[i%2][1])
        visited.add(positions[i%2])
    return len(visited)


assert A(sample_data) == 2, A(sample_data)
submit(A(data), part="a", day=3, year=2015)

assert B(sample_data) == 11, B(sample_data)
submit(B(data), part="b", day=3, year=2015)
