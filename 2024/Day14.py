import numpy as np
import aoc_utils.myconfig as utils
import re
import pandas as pd


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 14)


def part2():
    """After reading blog posts about this problem,
    I used where max value equals to 1,
    indicating all robots are in a unique position
    which finds the easter egg."""
    get_data = get_input_data(False).strip("\n").splitlines()
    sec = 7773  # Jump start solution to my known value but could start at 0 seconds.
    while True:
        sec += 1
        print(f"{sec=}")
        c_size = 101
        r_size = 103
        df = pd.DataFrame(
            np.zeros((r_size, c_size)), index=range(r_size), columns=range(c_size)
        )
        pat = "p=(?P<c>\d+),(?P<r>\d+) v=(?P<dc>-?\d+),(?P<dr>-?\d+)"
        for l in get_data:
            m = re.findall(pat, l)
            c, r, dc, dr = map(int, m[0])
            c_final = (c + (dc * sec)) % c_size
            r_final = (r + (dr * sec)) % r_size
            df.loc[r_final, c_final] += 1
        if np.max(df.to_numpy()) == 1:
            break
    return sec


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
