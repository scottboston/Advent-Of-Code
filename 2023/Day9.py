import numpy as np

import aoc_utils.myconfig as utils
from functools import reduce


def part1():
    input_data = utils.get_data(year=2023, day=9)
    total = 0
    for line in input_data.splitlines():
        a = np.array(line.split(), dtype=int)
        total += a[-1]
        while np.count_nonzero(a) != 0:
            a = np.diff(a)
            total += a[-1]
    results = total
    return results


def part2():
    input_data = utils.get_data(year=2023, day=9)
    total = 0
    for line in input_data.splitlines():
        a = np.array(line.split(), dtype=int)
        first = [a[0]]
        while np.count_nonzero(a) != 0:
            a = np.diff(a)
            first.append(a[0])
        total += reduce(lambda x, y: y - x, first[::-1])
    results = total
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
