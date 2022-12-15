#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp
import collections as cl

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=14))
sample_data: str = clean(
    """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
)


def try_add_sand(grid, sand):
    if grid[sand] == '.':
        grid[sand] = 'o'
        return True
    else:
        return False


def simulate(grid, sand):
    assert grid[sand] == 'o'

    if grid[(sand[0] + 1, sand[1])] == '.':
        grid[(sand[0] + 1, sand[1])] = 'o'
        grid[sand] = '.'
        return (sand[0] + 1, sand[1])

    if grid[(sand[0] + 1, sand[1] - 1)] == '.':
        grid[(sand[0] + 1, sand[1] - 1)] = 'o'
        grid[sand] = '.'
        return (sand[0] + 1, sand[1] - 1)

    if grid[(sand[0] + 1, sand[1]  + 1)] == '.':
        grid[(sand[0] + 1, sand[1] + 1)] = 'o'
        grid[sand] = '.'
        return (sand[0] + 1, sand[1] + 1)

    return sand


def A(input: str) -> int:
    grid = cl.defaultdict(lambda: '.')
    for structure in by_lines(input):
        paths = structure.split(" -> ")
        sy, sx = map(int, paths[0].split(","))
        for path in paths[1:]:
            ey, ex = map(int, path.split(","))
            if sx == ex:
                _sy, _ey = sorted((sy, ey))
                for y in range(_sy, _ey + 1):
                    grid[(sx, y)] = '#'
            elif sy == ey:
                _sx, _ex = sorted((sx, ex))
                for x in range(_sx, _ex + 1):
                    grid[(x, sy)] = '#'
            else:
                assert False, "Not a straight line"
            sx, sy = ex, ey

    maxy = max(grid.keys(), key=lambda x: x[0])[0]

    for i in it.count():
        sand = (0, 500)
        assert try_add_sand(grid, sand), "Cannot add more sand"
        while sand[0] < maxy + 2:
            _sand = simulate(grid, sand)
            if sand == _sand:
                break
            sand = _sand
        else:
            break

    return i



def B(input: str) -> int:
    grid = keydefaultdict(lambda x: '.')
    for structure in by_lines(input):
        paths = structure.split(" -> ")
        sy, sx = map(int, paths[0].split(","))
        for path in paths[1:]:
            ey, ex = map(int, path.split(","))
            if sx == ex:
                _sy, _ey = sorted((sy, ey))
                for y in range(_sy, _ey + 1):
                    grid[(sx, y)] = '#'
            elif sy == ey:
                _sx, _ex = sorted((sx, ex))
                for x in range(_sx, _ex + 1):
                    grid[(x, sy)] = '#'
            else:
                assert False, "Not a straight line"
            sx, sy = ex, ey

    maxy = max(grid.keys(), key=lambda x: x[0])[0]

    grid.default_factory = lambda x: '#' if x[0] == maxy + 2 else '.'

    for i in it.count():
        sand = (0, 500)
        if not try_add_sand(grid, sand):
            break
        while True:
            _sand = simulate(grid, sand)
            if sand == _sand:
                break
            sand = _sand

    return i


assert A(sample_data) == 24, A(sample_data)
submit(A(data), part="a", day=14, year=2022)

assert B(sample_data) == 93, B(sample_data)
submit(B(data), part="b", day=14, year=2022)
