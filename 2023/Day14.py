import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO
import numpy as np


def part1():
    input_data = utils.get_data(year=2023, day=14)
    df = pd.read_csv(StringIO(input_data), header=None)

    def move_o(x, y):
        if x < 1 or df.iloc[x - 1, y] in "O#":
            return
        df.iloc[x, y] = "."
        df.iloc[x - 1, y] = "O"
        return move_o(x - 1, y)

    df = df[0].apply(lambda x: pd.Series([*x]))
    r, c = np.where(df == "O")
    for x, y in zip(r, c):
        move_o(x, y)

    df = df.set_index(np.arange(df.shape[0], 0, -1))
    results = ((df == "O").sum(1) * df.index).sum()
    return results


def part2():
    input_data = utils.get_data(year=2023, day=14)
    results = None
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
