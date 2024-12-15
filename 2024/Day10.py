import pandas as pd
import networkx as nx
import numpy as np
from itertools import product
import aoc_utils.myconfig as utils

input_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 10)


def part1():
    a = np.array([[*l] for l in get_input_data(False).splitlines()])
    df = pd.DataFrame(a)
    df = df.astype("int")
    G = nx.DiGraph()

    r, c = np.where(df - df.shift() == 1)
    for i in zip(r, c):
        # print(f'{i[0] - 1, i[1]}->{i}')
        G.add_edge((i[0] - 1, i[1]), i)

    r, c = np.where(df - df.shift(-1) == 1)
    for i in zip(r, c):
        # print(f'({i[0] + 1},{i[1]})->{i}')
        G.add_edge((i[0] + 1, i[1]), i)

    r, c = np.where(df - df.shift(-1, axis=1) == 1)
    for i in zip(r, c):
        #         print(f'{i[0], i[1] + 1}->{i}')
        G.add_edge((i[0], i[1] + 1), i)

    r, c = np.where(df - df.shift(axis=1) == 1)
    for i in zip(r, c):
        #         print(f'{i[0], i[1] - 1}->{i}')
        G.add_edge((i[0], i[1] - 1), i)

    rs, cs = np.where(df == 0)
    re, ce = np.where(df == 9)

    th = zip(rs, cs)
    top = zip(re, ce)

    total = 0
    th_count = 0
    for i in product(th, top):
        if (l := len(list(nx.all_simple_paths(G, i[0], i[1])))) > 0:
            # print(i, l)
            total += l
            th_count += 1

    print(f"{th_count=}")

    result = th_count, total
    return result


def part2():
    return 'See Part I'


if __name__ == "__main__":
    print(f"Part1 and Part2 = {part1()}")
