from typing import Any, TypeVar, Optional

from multimethod import multimethod
from more_itertools import collapse


def clean(data: str) -> str:
    from textwrap import dedent

    return dedent(data.strip("\n"))


def by_groups(data: str, _sep: Optional[str]) -> list[str]:
    return data.split(_sep)


def by_lines(data: str) -> list[str]:
    return by_groups(data, _sep="\n")


def by_paragraphs(data: str) -> list[str]:
    return by_groups(data, _sep="\n\n")


def by_words(data: str) -> list[str]:
    return by_groups(data, _sep=None)


def by_chars(data: str) -> list[str]:
    return list(data)


_U = TypeVar("_U")


def to_type(data: list[str], _type: type[_U]) -> list[_U]:
    return lmap(_type, data)


def to_ints(data: list[str]) -> list[int]:
    return to_type(data, _type=int)


def to_floats(data: list[str]) -> list[float]:
    return to_type(data, _type=float)


@multimethod
def irange(stop: int) -> range:
    return range(stop + 1)


@multimethod
def irange(start: int, stop: int, step: int = 1) -> range:
    return range(start, stop + 1, step)


def lmap(*args, **kwargs) -> list[Any]:
    return list(map(*args, **kwargs))


def lfilter(*args, **kwargs) -> list[Any]:
    return list(filter(*args, **kwargs))


def lrange(*args, **kwargs) -> list[int]:
    return list(range(*args, **kwargs))


def lirange(*args, **kwargs) -> list[int]:
    return list(irange(*args, **kwargs))


def nested_split(data: str, *args):
    if not args:
        return data
    sep, *args = args
    return list(collapse(lmap(lambda x: nested_split(x, *args), data.split(sep))))


def from_ascii(ascii: str, padding = (0, 0)) -> str:
    """
    Convert ASCII art to a string
    """
    letters = {
        'A': clean("""
            .##.
            #..#
            #..#
            ####
            #..#
            #..#
        """),
        'B': [clean("""
            ###.
            #..#
            ###.
            #..#
            #..#
            ###.
        """), clean("""
            ###.
            #..#
            #..#
            ###.
            #..#
            ###.
        """)],
        'C': clean("""
            .##.
            #..#
            #...
            #...
            #..#
            .##.
        """),
        'D': clean("""
            ###.
            #..#
            #..#
            #..#
            #..#
            ###.
        """),
        'E': [clean("""
            ####
            #...
            ###.
            #...
            #...
            ####
        """), clean("""
            ####
            #...
            #...
            ###.
            #...
            ####
        """)],
        'F': [clean("""
            ####
            #...
            ###.
            #...
            #...
            #...
        """), clean("""
            ####
            #...
            #...
            ###.
            #...
            #...
        """)],
        'G': clean("""
            .##.
            #..#
            #...
            #.##
            #..#
            .###
        """),
        'H': [clean("""
            #..#
            #..#
            ####
            #..#
            #..#
            #..#
        """), clean("""
            #..#
            #..#
            #..#
            ####
            #..#
            #..#
        """)],
        'I': [clean("""
            .##.
            ..#.
            ..#.
            ..#.
            ..#.
            .##.
        """), clean("""
            .##.
            .#..
            .#..
            .#..
            .#..
            .##.
        """)],
        'J': clean("""
            ..##
            ...#
            ...#
            ...#
            #..#
            .##.
        """),
        'K': [clean("""
            #..#
            #.#.
            ##..
            #.#.
            #..#
            #..#
        """), clean("""
            #..#
            #..#
            #.#.
            ##..
            #.#.
            #..#
        """)],
        'L': clean("""
            #...
            #...
            #...
            #...
            #...
            ####
        """),
        'M': clean("""
        """),
        'N': clean("""
        """),
        'O': clean("""
            .##.
            #..#
            #..#
            #..#
            #..#
            .##.
        """),
        'P': clean("""
            ###.
            #..#
            #..#
            ###.
            #...
            #...
        """),
        'Q': clean("""
        """),
        'R': clean("""
            ###.
            #..#
            #..#
            ###.
            #.#.
            #..#
        """),
        'S': [clean("""
            .###
            #...
            .##.
            ...#
            ...#
            ###.
        """), clean("""
            .###
            #...
            #...
            .##.
            ...#
            ###.
        """)],
        'T': [clean("""
            ####
            ..#.
            ..#.
            ..#.
            ..#.
            ..#.
        """), clean("""
            ####
            .#..
            .#..
            .#..
            .#..
            .#..
        """)],
        'U': clean("""
            #..#
            #..#
            #..#
            #..#
            #..#
            .##.
        """),
        'V': clean("""
        """),
        'W': clean("""
        """),
        'X': clean("""
        """),
        'Y': clean("""
        """),
        'Z': clean("""
            ####
            ...#
            ..#.
            .#..
            #...
            ####
        """),
    }

    ascii = clean(ascii)
    lines = by_lines(ascii)
    height = len(lines)
    width = len(lines[0])
    result = ""
    for y in range(0, height, 6):
        for x in range(0, width, 4 + padding[0] + padding[1]):
            letter = ""
            for y2 in range(y, y + 6):
                for x2 in range(x + padding[0], x + 4 + padding[0]):
                    letter += lines[y2][x2]
                letter += "\n"
            for letter_name, letter_ascii in letters.items():
                if isinstance(letter_ascii, list):
                    if letter in letter_ascii:
                        result += letter_name
                        break
                else:
                    if letter == letter_ascii:
                        result += letter_name
                        break
            else:
                raise Exception(f"Could not find letter: {letter}")
        result += " "
    return result.strip()
