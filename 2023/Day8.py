import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO
from collections import Counter
import numpy as np


def part1():
    input_data = utils.get_data(year=2023, day=8)
    I = "LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR"
    df = pd.read_csv(StringIO(input_data), header=None, skiprows=2)
    df[["A", "L"]] = df[0].str.split("=|\(", expand=True)[[0, 2]]
    df["R"] = df[1].str.strip("\)")
    df = df.set_index("A")[["L", "R"]]
    df.index = df.index.str.strip()
    df["L"] = df["L"].str.strip()
    df["R"] = df["R"].str.strip()
    dfs = df.stack()
    row = "AAA"
    i = 0
    print(len(I))
    while row != "ZZZ":
        r = i % len(I)
        i += 1
        row = dfs.loc[row, I[r]]
        if i % 5_000 == 0:
            print(f"{i=} and {row=}")
    print(f"total {i=}")
    results = i

    return results


def part2():
    results = None
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
