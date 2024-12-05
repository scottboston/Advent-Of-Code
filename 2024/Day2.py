import pandas as pd
import numpy as np
import aoc_utils.myconfig as utils
from itertools import combinations

input_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

input_data = utils.get_data(2024, 2)


def part1():
    result = 0
    for l in input_data.splitlines():
        s = pd.Series(l.split())
        s = s.astype(int)
        s_diff = s.diff()
        x = s_diff[1:]
        result += ((abs(np.sign(x).sum()) == len(x)) & (abs(x) <= 3)).all()
    return result


def part2():
    result = 0
    for l in input_data.splitlines():
        s = pd.Series(l.split())
        s = s.astype(int)
        s_diff = s.diff()
        x = s_diff[1:]
        if ((abs(np.sign(x).sum()) == len(x)) & (abs(x) <= 3)).all():
            result += 1
        else:
            for c in list(combinations(s.index, len(s) - 1)):
                sub_s = s[list(c)]
                s_diff = sub_s.diff()
                x = s_diff[1:]
                if ((abs(np.sign(x).sum()) == len(x)) & (abs(x) <= 3)).all():
                    result += 1
                    break
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
