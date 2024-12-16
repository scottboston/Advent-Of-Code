import numpy as np
import aoc_utils.myconfig as utils
import re
import pandas as pd


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 14)


input_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def part1():
    sec = 100
    c_size = 101
    r_size = 103
    df = pd.DataFrame(
        np.zeros((r_size, c_size)), index=range(r_size), columns=range(c_size)
    )
    pat = "p=(?P<c>\d+),(?P<r>\d+) v=(?P<dc>-?\d+),(?P<dr>-?\d+)"
    for l in get_input_data(False).strip("\n").splitlines():
        m = re.findall(pat, l)
        c, r, dc, dr = map(int, m[0])
        c_final = (c + (dc * sec)) % c_size
        r_final = (r + (dr * sec)) % r_size
        df.loc[r_final, c_final] += 1
    q1 = df.loc[: df.shape[0] // 2 - 1, : df.shape[1] // 2 - 1].sum().sum()
    q2 = df.loc[: df.shape[0] // 2 - 1, df.shape[1] // 2 + 1 :].sum().sum()
    q3 = df.loc[df.shape[0] // 2 + 1 :, : df.shape[1] // 2 - 1].sum().sum()
    q4 = df.loc[df.shape[0] // 2 + 1 :, df.shape[1] // 2 + 1 :].sum().sum()
    return q1 * q2 * q3 * q4


def part2():
    sec = 0
    # while True:
    #     sec += 1
    #     c_size = 101
    #     r_size = 103
    #     df = pd.DataFrame(np.zeros((r_size, c_size)), index=range(r_size), columns=range(c_size))
    #     pat = "p=(?P<c>\d+),(?P<r>\d+) v=(?P<dc>-?\d+),(?P<dr>-?\d+)"
    #     for l in get_input_data(False).strip('\n').splitlines():
    #         m = re.findall(pat, l)
    #         print(m)
    #         c, r, dc, dr = map(int, m[0])
    #         c_final = (c + (dc * sec)) % c_size
    #         r_final = (r + (dr * sec)) % r_size
    #         df.loc[r_final, c_final] += 1
    #     print(df.astype(int))
    return "What??!?!?!?!?"


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
