import aoc_utils.myconfig as utils
import numpy as np
import nx_cugraph as nx
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
    a = np.array([[*l] for l in get_input_data(False).strip('\n').splitlines()])
    df = pd.DataFrame(a)
    dfr, dfc = df.shape
    print(f'{df.shape=}')
    G = nx.DiGraph()

    dft = df.isin(['.', 'S', 'E'])

    print('Start Shift1...')
    r, c = np.where(dft == dft.shift())
    for i in zip(r, c):
        # print(f'{i[0] - 1, i[1]}->{i}')
        G.add_edge((i[0] - 1, i[1]), i)

    print('Start Shift2...')
    r, c = np.where(dft == dft.shift(-1))
    for i in zip(r, c):
        # print(f'({i[0] + 1},{i[1]})->{i}')
        G.add_edge((i[0] + 1, i[1]), i)

    print('Start Shift3...')
    r, c = np.where(dft == dft.shift(-1, axis=1))
    for i in zip(r, c):
        #         print(f'{i[0], i[1] + 1}->{i}')
        G.add_edge((i[0], i[1] + 1), i)

    print('Shift Shift4...')
    r, c = np.where(dft == dft.shift(axis=1))
    for i in zip(r, c):
        #         print(f'{i[0], i[1] - 1}->{i}')
        G.add_edge((i[0], i[1] - 1), i)

    min_score = np.inf
    print('Start getting all paths')
    paths = list(nx.all_simple_edge_paths(G,(dfr-2,1), (1,dfc-2)))
    print('End get paths')

    print(f'{len(paths)=}')

    for path in tqdm(paths, ):
        dir_in = None
        score = 0
        for c, n in path:
            dir_out = 'r' if c[0] == n[0] else 'c'
            score += 1 if dir_out == dir_in else 1001
            if score >= min_score:
                break
            dir_in = dir_out
        min_score = min(min_score, score)

    result = min_score
    return result

if __name__ == '__main__':
    print(f'{part1()=}')