import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO


def part1():
    input_data = utils.get_data(year=2023, day=2)
    df = pd.read_csv(StringIO(input_data), sep=';', header=None, names=range(10))
    df = df.stack()
    df = pd.concat([(df.str.extractall(f'(?P<{c}>\d+) {c}').astype(int).le(n).groupby(level=0).all())
                for c, n in zip(['red', 'green', 'blue'],[12,13,14])], axis=1).all(1)
    df.index = df.index + 1
    results = sum(df.where(df).dropna().index.to_list())
    return results

def part2():
    input_data = utils.get_data(year=2023, day=2)
    df = pd.read_csv(StringIO(input_data), sep=';', header=None, names=range(10))
    df = df.stack()
    df = pd.concat([(df.str.extractall(f'(?P<{c}>\d+) {c}').astype(int))
                    for c, n in zip(['red', 'green', 'blue'], [12, 13, 14])], axis=1).groupby(level=0).max()
    results = df.prod(1).sum()
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
