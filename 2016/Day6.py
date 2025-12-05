import aoc_utils.myconfig as utils
import pandas as pd


def parts():
    input_data = utils.get_data(year=2016, day=6)
    df = pd.DataFrame([[*c] for c in input_data.splitlines()])
    part1 = "".join(df.apply(lambda x: x.mode()[0]).tolist())
    part2 = "".join(df.apply(lambda x: x.value_counts().idxmin()).tolist())
    return part1, part2


if __name__ == "__main__":
    print(parts())
