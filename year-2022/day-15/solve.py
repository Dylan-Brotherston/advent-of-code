#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp
import collections as cl

import z3

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=15))
sample_data: str = clean(
    """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
)


def A(input: str, target_row: int) -> int:
    visited = set()
    beacons = set()
    for line in by_lines(input):
        m = re.fullmatch(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        SensorX, SensorY, BeaconX, BeaconY = map(int, m.groups())
        beacons.add((BeaconX, BeaconY))
        distance = abs(SensorX - BeaconX) + abs(SensorY - BeaconY)

        for dx in (-1, 1):
            d = abs(SensorY - target_row)
            x = SensorX
            while d <= distance:
                visited.add((x, target_row))
                x += dx
                d += 1

    return len(visited - beacons)


def B(input: str, limit: int) -> int:
    pairs = []
    beacons = set()
    for line in by_lines(input):
        m = re.fullmatch(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        SensorX, SensorY, BeaconX, BeaconY = map(int, m.groups())
        beacons.add((BeaconX, BeaconY))
        distance = abs(SensorX - BeaconX) + abs(SensorY - BeaconY)
        pairs.append((SensorX, SensorY, BeaconX, BeaconY, distance))


    s = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    s.add(0 <= x)
    s.add(x <= limit)
    s.add(0 <= y)
    s.add(y <= limit)

    def z3_abs(x):
        return z3.If(x >= 0, x, -x)

    for SensorX, SensorY, BeaconX, BeaconY, distance in pairs:
        s.add(z3_abs(SensorX - x) + z3_abs(SensorY - y) > distance)

    s.check()
    return s.model().eval(x * 4000000 + y)


assert A(sample_data, 10) == 26, A(sample_data, 10)
submit(A(data, 2000000), part="a", day=15, year=2022)

assert B(sample_data, 20) == 56000011, B(sample_data, 20)
submit(B(data, 4000000), part="b", day=15, year=2022)
