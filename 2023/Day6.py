import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO
import numpy as np


def part1():
    input_data = utils.get_data(year=2023, day=5)
    Time = [48, 93, 85, 95]
    Distance = [296, 1928, 1236, 1391]

    beat = []
    for i in range(4):
        d = Time[i]
        s = 0
        for x in range(0, d + 1):
            if (d - x) * x > Distance[i]:
                s += 1
        beat.append(s)
    return np.prod(beat)


def part2():
    Time = 48938595
    Distance = 296192812361391
    for i in range(0, Time + 1):
        if (Time - i) * i > Distance:
            break
    up = i

    for i in range(Time + 1, 0, -1):
        if (Time - i) * i > Distance:
            print(i)
            break
    down = i

    results = down - up + 1
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
