import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO


def part1():
    input_data = utils.get_data(year=2023, day=5)

    df = pd.read_csv(StringIO(input_data), header=None, names=["maps"])
    seeds = df.iloc[0, 0].split(": ")[1].split(" ")
    df = df.iloc[1:]

    categories = df.loc[df.iloc[:, 0].str.contains(":"), "maps"].str.split(" ").str[0]
    df = df.assign(group=categories)
    df["group"] = df["group"].ffill()
    df = df[~df.iloc[:, 0].str.contains(":")]

    df_maps = dict(tuple(df.groupby("group")))

    def df_to_dict(df, v):
        ll = df["maps"].str.split(" ", expand=True).astype(float).to_numpy().tolist()
        s = pd.concat(
            [
                pd.Series(e, pd.IntervalIndex.from_tuples([(s, s + i - 1)]))
                for e, s, i in ll
            ]
        )
        try:
            return v - s.index[s.index.get_loc(v)].left + s.get(v)
        except KeyError:
            return v

    location = []
    for s in seeds:
        s = int(s)
        for _, m in categories.items():
            s = df_to_dict(df_maps[m], s)
            print(f"{m}-{s}")
        location.append(s)

    results = int(min(location))
    return results


def part2():
    input_data = utils.get_data(year=2023, day=5)
    results = None
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
