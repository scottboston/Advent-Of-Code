import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
import pandas as pd

input_data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 18)


def part1():
    df = pd.DataFrame(np.ones((71, 71)))
    for e in get_input_data(False).strip("\n").splitlines()[:1024]:
        c, r = map(int, e.split(","))
        df.iloc[r, c] = 0
    G = nx.Graph()

    r, c = np.where((df == 1.0) & (df.shift() == 1.0))
    for i in zip(r, c):
        G.add_edge((i[0] - 1, i[1]), (i[0], i[1]))

    r, c = np.where((df == 1.0) & (df.shift(-1) == 1.0))
    for i in zip(r, c):
        G.add_edge((i[0] + 1, i[1]), (i[0], i[1]))

    r, c = np.where((df == 1.0) & (df.shift(-1, axis=1) == 1.0))
    for i in zip(r, c):
        G.add_edge((i[0], i[1] + 1), (i[0], i[1]))

    r, c = np.where((df == 1.0) & (df.shift(axis=1) == 1.0))
    for i in zip(r, c):
        G.add_edge((i[0], i[1] - 1), (i[0], i[1]))

    path = nx.shortest_path(G, (0, 0), (70, 70))
    result = len(path) - 1
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
