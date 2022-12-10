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


data: str = clean(get_data(year=2022, day=10))
sample_data: str = clean(
    """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
)


def A(input: str) -> int:
    total = 0
    register = 1
    instructions = by_lines(input)
    current_instruction = instructions.pop(0)
    for cycle in it.count(1):

        if cycle in [20, 60, 100, 140, 180, 220]:
            total += cycle * register

        if len(instructions) == 0:
            break

        if current_instruction.startswith("noop"):
            current_instruction = instructions.pop(0)
            continue

        if current_instruction.startswith("addx"):
            _, value = current_instruction.split()
            value = int(value)
            current_instruction = '!addx-continue'
            continue

        if current_instruction.startswith("!addx-continue"):
            register += value
            current_instruction = instructions.pop(0)
            continue

    return total

sample_output = '''\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''

def B(input: str) -> str:
    solution = ""
    register = 1
    counter = 0
    instructions = by_lines(input)
    current_instruction = instructions.pop(0)
    for pixel in it.count():
        if register == pixel % 40:
            solution += '#'
        elif register != 0 and register == (pixel % 40) - 1:
            solution += '#'
        elif register != 40 and register == (pixel % 40) + 1:
            solution += '#'
        else:
            solution += '.'

        counter += 1

        if counter == 40:
            solution += '\n'
            counter = 0

        if len(instructions) == 0:
            break

        if current_instruction.startswith("noop"):
            current_instruction = instructions.pop(0)
            continue

        if current_instruction.startswith("addx"):
            _, value = current_instruction.split()
            value = int(value)
            current_instruction = '!addx-continue'
            continue

        if current_instruction.startswith("!addx-continue"):
            register += value
            current_instruction = instructions.pop(0)
            continue

    return solution


assert A(sample_data) == 13140, A(sample_data)
submit(A(data), part="a", day=10, year=2022)

assert B(sample_data) == sample_output, B(sample_data)
submit(from_ascii(B(data), (0, 1)), part="b", day=10, year=2022)
