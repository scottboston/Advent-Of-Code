import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO


def part1():
    input_data = utils.get_data(year=2023, day=1)
    s = pd.read_csv(StringIO(input_data), header=None).squeeze()
    n = s.str.extractall("(\d)").unstack()
    return n.apply(
        lambda x: int(x.iloc[0] + x.iloc[x.last_valid_index()[1]]), axis=1
    ).sum()


def part2():
    input_data = utils.get_data(year=2023, day=1)
    input_data = (
        input_data.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )
    s = pd.read_csv(StringIO(input_data), header=None).squeeze()
    n = s.str.extractall("(\d)").unstack()
    t = n.apply(lambda x: int(x.iloc[0] + x.iloc[x.last_valid_index()[1]]), axis=1)

    return t.sum()


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
