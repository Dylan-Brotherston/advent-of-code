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

from textwrap import dedent, indent
from aocd import get_data, submit  # type: ignore
from share import *


puzzle_data: str = clean(get_data(year=2015, day=7))
sample_data: dict[str, list[tuple[str, int]]] = {
    "A": [
    ],
    "B": [
    ],
}


def emulate(input: str, wires: dict[str, int]):
    while "a" not in wires:
        for line in input.splitlines():
            try:
                if m := re.fullmatch(r"(\w+) -> (\w+)", line):
                    if m.group(2) not in wires:
                        try:
                            wires[m.group(2)] = int(m.group(1))
                        except ValueError:
                            wires[m.group(2)] = wires[m.group(1)]
                elif m := re.fullmatch(r"(\w+) AND (\w+) -> (\w+)", line):
                    try:
                        wires[m.group(3)] = int(m.group(1)) & int(m.group(2))
                    except ValueError:
                        try:
                            wires[m.group(3)] = int(m.group(1)) & wires[m.group(2)]
                        except ValueError:
                            try:
                                wires[m.group(3)] = wires[m.group(1)] & int(m.group(2))
                            except ValueError:
                                wires[m.group(3)] = wires[m.group(1)] & wires[m.group(2)]
                elif m := re.fullmatch(r"(\w+) OR (\w+) -> (\w+)", line):
                    try:
                        wires[m.group(3)] = int(m.group(1)) | int(m.group(2))
                    except ValueError:
                        try:
                            wires[m.group(3)] = int(m.group(1)) | wires[m.group(2)]
                        except ValueError:
                            try:
                                wires[m.group(3)] = wires[m.group(1)] | int(m.group(2))
                            except ValueError:
                                wires[m.group(3)] = wires[m.group(1)] | wires[m.group(2)]
                elif m := re.fullmatch(r"(\w+) LSHIFT (\d+) -> (\w+)", line):
                    try:
                        wires[m.group(3)] = int(m.group(1)) << int(m.group(2))
                    except ValueError:
                        try:
                            wires[m.group(3)] = int(m.group(1)) << wires[m.group(2)]
                        except ValueError:
                            try:
                                wires[m.group(3)] = wires[m.group(1)] << int(m.group(2))
                            except ValueError:
                                wires[m.group(3)] = wires[m.group(1)] << wires[m.group(2)]
                elif m := re.fullmatch(r"(\w+) RSHIFT (\d+) -> (\w+)", line):
                    try:
                        wires[m.group(3)] = int(m.group(1)) >> int(m.group(2))
                    except ValueError:
                        try:
                            wires[m.group(3)] = int(m.group(1)) >> wires[m.group(2)]
                        except ValueError:
                            try:
                                wires[m.group(3)] = wires[m.group(1)] >> int(m.group(2))
                            except ValueError:
                                wires[m.group(3)] = wires[m.group(1)] >> wires[m.group(2)]
                elif m := re.fullmatch(r"NOT (\w+) -> (\w+)", line):
                    wires[m.group(2)] = ~wires[m.group(1)] & 0xffff
                else:
                    raise ValueError(f"invalid line: {line}")
            except KeyError:
                pass


def A(input: str) -> int:
    wires = {}
    emulate(input, wires)

    return wires["a"]

def B(input: str) -> int:
    wires = {}
    emulate(input, wires)

    a = wires["a"]
    wires = {}
    wires["b"] = a
    emulate(input, wires)

    return wires["a"]

for data, solution in sample_data["A"]:
    assert (recived := A(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(A(puzzle_data), part="a", day=7, year=2015)

for data, solution in sample_data["B"]:
    assert (recived := B(data)) == solution, f"\nexpected:\n{indent(str(solution), '\t')}\n\nrecived:\n{indent(str(recived), '\t')}"
submit(B(puzzle_data), part="b", day=7, year=2015)
