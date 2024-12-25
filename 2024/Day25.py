import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
import pandas as pd
import re
from itertools import combinations
from collections import deque
from itertools import product

input_data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 25)


def part1():
    list_rows = []
    i = 0
    df_dict = {i: pd.DataFrame()}
    for l in get_input_data(False).strip("\n").splitlines():
        if l == "":
            df_dict[i] = pd.concat(
                [df_dict.get(i, pd.DataFrame()), pd.DataFrame(list_rows)]
            )
            list_rows = []
            i += 1
        else:
            list_rows.append([*l])
    df_dict[i] = pd.concat([df_dict.get(i, pd.DataFrame()), pd.DataFrame(list_rows)])

    df_bottom = []
    df_top = []
    for k, df in df_dict.items():
        df = df.mask(df == ".").notna().astype(int)
        if df.iloc[0].sum() == 0:
            df_bottom.append(df)
        else:
            df_top.append(df)

    result = sum(1 for b, t in product(df_bottom, df_top) if (b + t).max().max() == 1)

    return result


if __name__ == "__main__":
    print(f"{part1()=}")
