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


data: str = clean(get_data(year=2022, day=2))
sample_data: str = clean(
    """
A Y
B X
C Z
"""
)

opponent_move_map: dict[str, str] = {
    "A": "R",
    "B": "P",
    "C": "S",
}

player_move_map: dict[str, str] = {
    "X": "R",
    "Y": "P",
    "Z": "S",
}

shape_score_map: dict[str, int] = {
    "R": 1,
    "P": 2,
    "S": 3,
}

outcome_score_map: dict[str, int] = {
    "L": 0,
    "D": 3,
    "W": 6,
}

hand_outcome_map: dict[tuple[str, str], str] = {
    ("R", "R"): "D",
    ("R", "P"): "W",
    ("R", "S"): "L",
    ("P", "R"): "L",
    ("P", "P"): "D",
    ("P", "S"): "W",
    ("S", "R"): "W",
    ("S", "P"): "L",
    ("S", "S"): "D",
}


def A(input: str) -> int:
    total = 0
    for line in by_lines(input):
        opponent_move, player_move = line.split()

        outcome = hand_outcome_map[
            (opponent_move_map[opponent_move], player_move_map[player_move])
        ]

        total += (
            shape_score_map[player_move_map[player_move]] + outcome_score_map[outcome]
        )

    return total


payer_outcome_map: dict[str, str] = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

player_shape_map: dict[tuple[str, str], str] = {
    ("R", "W"): "P",
    ("R", "L"): "S",
    ("R", "D"): "R",
    ("P", "W"): "S",
    ("P", "L"): "R",
    ("P", "D"): "P",
    ("S", "W"): "R",
    ("S", "L"): "P",
    ("S", "D"): "S",
}


def B(input: str) -> int:
    total = 0
    for line in by_lines(input):
        opponent_move, outcome = line.split()

        player_move = player_shape_map[
            (opponent_move_map[opponent_move], payer_outcome_map[outcome])
        ]

        total += (
            shape_score_map[player_move] + outcome_score_map[payer_outcome_map[outcome]]
        )

    return total


assert A(sample_data) == 15, A(sample_data)
submit(A(data), part="a", day=2, year=2022)

assert B(sample_data) == 12, B(sample_data)
submit(B(data), part="b", day=2, year=2022)
