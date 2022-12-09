#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=9))
sample_data: str = clean(
    """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
)


def A(input: str) -> int:
    visited = {(0, 0),}
    cord = [(0, 0) for _ in range(2)]

    for line in by_lines(input):
        direction, distance = line.split()
        distance = int(distance)

        for _ in range(distance):
            match direction:
                case "U":
                    cord[0] = (cord[0][0], cord[0][1] + 1)
                case "D":
                    cord[0] = (cord[0][0], cord[0][1] - 1)
                case "L":
                    cord[0] = (cord[0][0] - 1, cord[0][1])
                case "R":
                    cord[0] = (cord[0][0] + 1, cord[0][1])

            diff = (cord[0][0] - cord[1][0], cord[0][1] - cord[1][1])

            if diff == (2, 0):
                cord[1] = (cord[1][0] + 1, cord[1][1])
            if diff == (-2, 0):
                cord[1] = (cord[1][0] - 1, cord[1][1])
            if diff == (0, 2):
                cord[1] = (cord[1][0], cord[1][1] + 1)
            if diff == (0, -2):
                cord[1] = (cord[1][0], cord[1][1] - 1)
            if diff == (2, 1):
                cord[1] = (cord[1][0] + 1, cord[1][1] + 1)
            if diff == (2, -1):
                cord[1] = (cord[1][0] + 1, cord[1][1] - 1)
            if diff == (-2, 1):
                cord[1] = (cord[1][0] - 1, cord[1][1] + 1)
            if diff == (-2, -1):
                cord[1] = (cord[1][0] - 1, cord[1][1] - 1)
            if diff == (1, 2):
                cord[1] = (cord[1][0] + 1, cord[1][1] + 1)
            if diff == (-1, 2):
                cord[1] = (cord[1][0] - 1, cord[1][1] + 1)
            if diff == (1, -2):
                cord[1] = (cord[1][0] + 1, cord[1][1] - 1)
            if diff == (-1, -2):
                cord[1] = (cord[1][0] - 1, cord[1][1] - 1)

            visited.add(cord[-1])

    return len(visited)


def B(input: str) -> int:
    # Same as A, but with a rope of length 10 instead of 2
    visited = {(0, 0),}
    cord = [(0, 0) for _ in range(10)]

    for line in by_lines(input):
        direction, distance = line.split()
        distance = int(distance)

        for _ in range(distance):
            match direction:
                case "U":
                    cord[0] = (cord[0][0], cord[0][1] + 1)
                case "D":
                    cord[0] = (cord[0][0], cord[0][1] - 1)
                case "L":
                    cord[0] = (cord[0][0] - 1, cord[0][1])
                case "R":
                    cord[0] = (cord[0][0] + 1, cord[0][1])

            for i in range(1, 10):
                diff = (cord[i - 1][0] - cord[i][0], cord[i - 1][1] - cord[i][1])

                if diff == (2, 0):
                    cord[i] = (cord[i][0] + 1, cord[i][1])
                if diff == (-2, 0):
                    cord[i] = (cord[i][0] - 1, cord[i][1])
                if diff == (0, 2):
                    cord[i] = (cord[i][0], cord[i][1] + 1)
                if diff == (0, -2):
                    cord[i] = (cord[i][0], cord[i][1] - 1)
                if diff == (2, 1):
                    cord[i] = (cord[i][0] + 1, cord[i][1] + 1)
                if diff == (2, -1):
                    cord[i] = (cord[i][0] + 1, cord[i][1] - 1)
                if diff == (-2, 1):
                    cord[i] = (cord[i][0] - 1, cord[i][1] + 1)
                if diff == (-2, -1):
                    cord[i] = (cord[i][0] - 1, cord[i][1] - 1)
                if diff == (1, 2):
                    cord[i] = (cord[i][0] + 1, cord[i][1] + 1)
                if diff == (-1, 2):
                    cord[i] = (cord[i][0] - 1, cord[i][1] + 1)
                if diff == (1, -2):
                    cord[i] = (cord[i][0] + 1, cord[i][1] - 1)
                if diff == (-1, -2):
                    cord[i] = (cord[i][0] - 1, cord[i][1] - 1)
                if diff == (2, 2):
                    cord[i] = (cord[i][0] + 1, cord[i][1] + 1)
                if diff == (-2, -2):
                    cord[i] = (cord[i][0] - 1, cord[i][1] - 1)
                if diff == (2, -2):
                    cord[i] = (cord[i][0] + 1, cord[i][1] - 1)
                if diff == (-2, 2):
                    cord[i] = (cord[i][0] - 1, cord[i][1] + 1)

            visited.add(cord[-1])

    return len(visited)


assert A(sample_data) == 13, A(sample_data)
submit(A(data), part="a", day=9, year=2022)

assert B(sample_data) == 1, B(sample_data)
submit(B(data), part="b", day=9, year=2022)
