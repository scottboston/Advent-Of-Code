import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
import pandas as pd
from tqdm import tqdm

input_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

input_data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 16)


def part1():
    a = np.array([[*l] for l in get_input_data(False).strip("\n").splitlines()])
    df = pd.DataFrame(a)
    dfr, dfc = df.shape
    directions = ["^", ">", "v", "<"]
    G = nx.Graph()

    dft = df.isin([".", "S", "E"])

    r, c = np.where(dft == dft.shift())
    for i in zip(r, c):
        [
            G.add_edge(
                (i[0], i[1], directions[d]),
                (i[0], i[1], directions[(d + 1) % 4]),
                weight=1000,
            )
            for d in range(4)
        ]
        G.add_edge((i[0] - 1, i[1], "v"), (i[0], i[1], "v"), weight=1)

    r, c = np.where(dft == dft.shift(-1))
    for i in zip(r, c):
        [
            G.add_edge(
                (i[0], i[1], directions[d]),
                (i[0], i[1], directions[(d + 1) % 4]),
                weight=1000,
            )
            for d in range(4)
        ]
        G.add_edge((i[0] + 1, i[1], "^"), (i[0], i[1], "^"), weight=1)

    r, c = np.where(dft == dft.shift(-1, axis=1))
    for i in zip(r, c):
        [
            G.add_edge(
                (i[0], i[1], directions[d]),
                (i[0], i[1], directions[(d + 1) % 4]),
                weight=1000,
            )
            for d in range(4)
        ]
        G.add_edge((i[0], i[1] + 1, "<"), (i[0], i[1], "<"), weight=1)

    r, c = np.where(dft == dft.shift(axis=1))
    for i in zip(r, c):
        #         print(f'{i[0], i[1] - 1}->{i}')
        [
            G.add_edge(
                (i[0], i[1], directions[d]),
                (i[0], i[1], directions[(d + 1) % 4]),
                weight=1000,
            )
            for d in range(4)
        ]
        G.add_edge((i[0], i[1] - 1, ">"), (i[0], i[1], ">"), weight=1)

    [G.add_edge((1, dfc - 2, directions[d]), (1, dfc - 2), weight=0) for d in range(4)]

    print(G)
    paths = nx.single_source_dijkstra(
        G, source=(dfr - 2, 1, ">"), target=(1, dfc - 2), weight="weight"
    )

    result = paths[0]

    return result


if __name__ == "__main__":
    print(f"{part1()=}")
