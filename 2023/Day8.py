import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO
from collections import Counter
import numpy as np
import math


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
    while row != "ZZZ":
        r = i % len(I)
        i += 1
        row = dfs.loc[row, I[r]]
    results = i

    return results


def part2_func(row, dfs):
    I = "LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR"
    i = 0
    while row[2] != "Z":
        r = i % len(I)
        i += 1
        row = dfs.loc[row, I[r]]
    results = i

    return results


def part2():
    input_data = utils.get_data(year=2023, day=8)
    df = pd.read_csv(StringIO(input_data), header=None, skiprows=2)
    df[["A", "L"]] = df[0].str.split("=|\(", expand=True)[[0, 2]]
    df["R"] = df[1].str.strip("\)")
    df = df.set_index("A")[["L", "R"]]
    df.index = df.index.str.strip()
    df["L"] = df["L"].str.strip()
    df["R"] = df["R"].str.strip()
    dfs = df.stack()
    rows = df[dfs.index.levels[0].str[2] == "A"].index.tolist()
    i = []
    for row in rows:
        i.append(part2_func(row, dfs))
    results = math.lcm(*i)
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
