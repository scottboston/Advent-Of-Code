from io import StringIO
import pandas as pd
import aoc_utils.myconfig as utils


def part1():
    input = utils.get_data(2024, 1)
    df = pd.read_csv(StringIO(input), sep=r"\s+", header=None)
    df.columns = ["x", "y"]

    df["X"] = df["x"].sort_values().to_numpy()
    df["Y"] = df["y"].sort_values().to_numpy()

    df["eval"] = df.eval("X-Y").abs()
    results = df["eval"].sum()
    return results


def part2():
    input = utils.get_data(2024, 1)
    df = pd.read_csv(StringIO(input), sep=r"\s+", header=None)
    df.columns = ["x", "y"]

    vc = df["y"].value_counts()
    results = df["x"].apply(lambda x: vc.get(x, 0) * x).sum()
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
