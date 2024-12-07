import aoc_utils.myconfig as utils
import pandas as pd
import numpy as np
from joblib import Parallel, delayed
from functools import partial
from tqdm import tqdm


class LoopException(Exception):
    pass


input_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

input_data = utils.get_data(2024, 6)


# Setup directions
N = (-1, 0)
W = (0, -1)
S = (1, 0)
E = (0, 1)
direction = [N, E, S, W]
dir_sym = ["^", ">", "v", "<"]


def part1():
    a = np.array([[*l] for l in input_data.splitlines()])
    df = pd.DataFrame(a)

    startpos = np.where(df == "^")
    r = startpos[0][0]
    c = startpos[1][0]
    turn = 0
    dir = direction[turn]

    while True:
        try:
            r, c, df, dir, turn = move(df, r, c, dir, turn)
            # print('\n')
        except KeyError as ke:
            print("Left Area")
            break
    print(f"{turn=}")
    return df.stack().isin(dir_sym).sum(), df


def move(df, r, c, dir, turn):
    while df.loc[r + dir[0], c + dir[1]] in ["."] + dir_sym:
        r += dir[0]
        c += dir[1]
        df.loc[r, c] = dir_sym[turn % 4]
    turn += 1
    df.loc[r, c] = dir_sym[turn % 4]
    dir = direction[turn % 4]
    return r, c, df, dir, turn


def move2(df, r, c, dir, turn):
    if df.loc[r + dir[0], c + dir[1]] == dir_sym[turn % 4] or turn > 200:
        raise LoopException
    while df.loc[r + dir[0], c + dir[1]] in ["."] + dir_sym:
        r += dir[0]
        c += dir[1]
        df.loc[r, c] = dir_sym[turn % 4]
    turn += 1
    df.loc[r, c] = dir_sym[turn % 4]
    dir = direction[turn % 4]
    return r, c, df, dir, turn


def part2():
    a = np.array([[*l] for l in input_data.splitlines()])
    df = pd.DataFrame(a)

    startpos = np.where(df == "^")
    r = startpos[0][0]
    c = startpos[1][0]
    turn = 0
    dir = direction[turn]

    l_dfs = []
    _, dfin = part1()
    ri, ci = np.where(dfin.isin(dir_sym))

    for i in zip(ri, ci):
        df_in = df.copy()
        df_in.loc[i[0], i[1]] = "#"
        l_dfs.append(df_in)
    pfunc = partial(run_guard, r, c, dir, turn)
    runs = Parallel(n_jobs=-1)(delayed(pfunc)(df_input) for df_input in tqdm(l_dfs))
    guard_loop = sum(runs)

    # guard_loop += run_guard(df, r, c, dir, turn)
    return guard_loop


def run_guard(r, c, dir, turn, df):
    while True:
        try:
            r, c, df, dir, turn = move2(df, r, c, dir, turn)
        except KeyError as ke:
            del df
            return 0
        except LoopException as le:
            # print(f'Loop found')
            del df
            return 1


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
