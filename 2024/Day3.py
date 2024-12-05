import pandas as pd
import numpy as np
import aoc_utils.myconfig as utils
import re

input_data = utils.get_data(year=2024, day=3)


def part1():
    pat = "mul\((\d+),(\d+)\)"
    match = re.findall(pat, input_data)
    result = sum(int(i) * int(j) for i, j in match)
    return result


def part2():
    pat = "(do(?:n't)?)|mul\((\d+),(\d+)\)"
    match = re.findall(pat, input_data)
    df = pd.DataFrame(match, columns=["include", "i", "j"])
    df["flag"] = df["include"].map({"don't": 0, "do": 1, "": np.nan})
    df.loc[: df["flag"].first_valid_index(), "flag"] = df.loc[
        : df["flag"].first_valid_index()
    ].fillna(1)
    df = df.ffill()
    result = (
        df.loc[df["include"].eq("") & (df["flag"].eq(1)), ["i", "j"]]
        .astype(int)
        .eval("i*j")
        .sum()
    )
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
