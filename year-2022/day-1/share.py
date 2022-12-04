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
