#! /usr/bin/env python3

import itertools as it
import more_itertools as mit
import functools as ft
import os.path as op
import regex as re
import numpy as np
import urllib3 as ul
import dateutil.parser as dp

from typing import Generator

from aocd import get_data, submit  # type: ignore

from share import *


PLACEHOLDER: object = object()


data: str = clean(get_data(year=2022, day=7))
sample_data: str = clean(
    """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
)


def A(input: str) -> int:
    file_sys: dict[str, dict[str, dict | int] | int] = {}
    path = "/"
    for line in input.splitlines():
        if line.startswith("$ cd "):
            line = line[5:]
            if line.startswith("/"):
                path = line
            else:
                path = op.join(path, line)
            path = op.normpath(path)
        elif line.startswith("$ ls"):
            pass
        else:
            if line.startswith("dir "):
                continue
            size, name = line.split()
            fs: dict[str, dict[str, dict | int] | int] = file_sys
            for part in filter(None, path.split("/")):
                if part not in fs:
                    fs[part] = {}
                fs: dict[str, dict[str, dict | int] | int] = fs[part]
            fs[name] = int(size)

    def dir_size(fs: dict[str, dict | int]) -> int:
        return sum(
            size if isinstance(size, int) else dir_size(size)
            for size in fs.values()
        )

    def all_dir_sizes(fs: dict[str, dict | int]) -> Generator[int, None, None]:
        yield dir_size(fs)
        for size in fs.values():
            if isinstance(size, dict):
                yield from all_dir_sizes(size)

    return sum(filter(lambda x: x < 100000, all_dir_sizes(file_sys)))


def B(input: str) -> int:
    file_sys: dict[str, dict[str, dict | int] | int] = {}
    path = "/"
    for line in input.splitlines():
        if line.startswith("$ cd "):
            line = line[5:]
            if line.startswith("/"):
                path = line
            else:
                path = op.join(path, line)
            path = op.normpath(path)
        elif line.startswith("$ ls"):
            pass
        else:
            if line.startswith("dir "):
                continue
            size, name = line.split()
            fs: dict[str, dict[str, dict | int] | int] = file_sys
            for part in filter(None, path.split("/")):
                if part not in fs:
                    fs[part] = {}
                fs: dict[str, dict[str, dict | int] | int] = fs[part]
            fs[name] = int(size)

    def dir_size(fs):
        return sum(
            size if isinstance(size, int) else dir_size(size)
            for size in fs.values()
        )

    def all_dir_sizes(fs):
        yield dir_size(fs)
        for size in fs.values():
            if isinstance(size, dict):
                yield from all_dir_sizes(size)

    total_size = dir_size(file_sys)
    unused_size = 70000000 - total_size
    need_to_delete = 30000000 - unused_size

    return min(list(filter(lambda x: x >= need_to_delete, all_dir_sizes(file_sys))))


assert A(sample_data) == 95437, A(sample_data)
submit(A(data), part="a", day=7, year=2022)

assert B(sample_data) == 24933642, B(sample_data)
submit(B(data), part="b", day=7, year=2022)
