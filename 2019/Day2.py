import numpy as np
from io import StringIO
import pandas as pd
import aoc_utils.myconfig as utils
import operator


# input_data = """1,9,10,3,2,3,11,0,99,30,40,50"""
# input_data = """1,0,0,0,99"""
# input_data = """2,3,0,3,99"""
# input_data = """2,4,4,5,99,0"""
# input_data = """1,1,1,4,99,5,6,0,99"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2019, 2)


def part1():
    a = np.array([int(x) for x in get_input_data(False).split(",")], dtype="int64")
    a[1] = 12
    a[2] = 2
    for i in range(0, len(a) + 1, 4):
        r = a[i : i + 4]
        print(r)
        if r[0] == 99:
            break
        elif r[0] == 1:
            a[r[3]] = a[r[1]] + a[r[2]]
        else:
            a[r[3]] = a[r[1]] * a[r[2]]
    result = a[0]
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
