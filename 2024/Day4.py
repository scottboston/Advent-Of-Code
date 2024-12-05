import pandas as pd
import numpy as np
import aoc_utils.myconfig as utils
import re


input_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

input_data = utils.get_data(year=2024, day=4)

def part1():
    a = np.array([[*l] for l in input_data.splitlines()])
    df = pd.DataFrame(a)
    dfs = df.stack()
    rx, cx = np.where(df == 'X')
    result = 0
    for r, c in zip(rx, cx):
        try:
            result += checkpat(dfs, [r,r,r,r], [c+0,c+1,c+2,c+3], [*'XMAS'])
            result += checkpat(dfs, [r+0,r+1,r+2,r+3], [c,c,c,c], [*'XMAS'])
            result += checkpat(dfs, [r+0,r+1,r+2,r+3], [c+0,c+1,c+2,c+3], [*'XMAS'])
            result += checkpat(dfs, [r-3, r-2, r-1, r], [c-3, c-2, c-1, c], [*'SAMX'])
            result += checkpat(dfs, [r-3, r-2, r-1, r], [c+3, c+2, c+1, c], [*'SAMX'])
            result += checkpat(dfs, [r+3, r+2, r+1, r], [c-3, c-2, c-1, c], [*'SAMX'])
            result += checkpat(dfs, [r,r,r,r], [c-3,c-2,c-1,c], [*'SAMX'])
            result += checkpat(dfs, [r-3,r-2,r-1,r], [c,c,c,c], [*'SAMX'])
        except:
            pass
    return result

def checkpat(dfs, r, c, pat):
    try:
        # print(dfs.loc[zip(r,c)])
        checked = (dfs.loc[zip(r,c)] == pat).all()
    except:
        checked = 0
    return checked

def part2():
    a = np.array([[*l] for l in input_data.splitlines()])
    df = pd.DataFrame(a)
    df_check = pd.DataFrame([[*'M.S'],
                             [*'.A.'],
                             [*'M.S']])

    r_df, c_df = df.shape
    result = 0
    for r in range(r_df):
        for c in range(c_df):
            try:
                sub_df = df.loc[r:r+2,c:c+2]
                if sub_df.size == 9:
                    result += max(np.diag(np.rot90(sub_df.to_numpy(), k) == df_check.to_numpy()).all() &
                        np.diag(np.rot90(np.rot90(sub_df.to_numpy(), k) == df_check.to_numpy())).all()
                        for k in range(4))
            except:
                pass
    return result


if __name__ == '__main__':
    # print(f'{part1()=}')
    print(f'{part2()=}')