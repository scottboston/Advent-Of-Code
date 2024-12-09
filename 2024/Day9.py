import aoc_utils.myconfig as utils
import numpy as np


input_data = """2333133121414131402"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 9).strip("\n")


def part1():
    disk_map = np.array([*get_input_data(False)], dtype=np.int64)
    repeats = disk_map.astype(np.int64)
    files = disk_map.copy().astype(str)
    files[1::2] = "."
    files[::2] = np.cumsum(files == ".").astype(str)[::2]
    files = np.repeat(files, repeats)
    i_dot = np.where(files == ".")[0]
    rev_files = files[files != "."][::-1]
    files[i_dot] = rev_files[: len(i_dot)]
    files = files[: -len(i_dot)]
    result = np.sum(files.astype(np.int64) * np.arange(len(files)))
    return result


def part2():
    disk_map = np.array([*get_input_data(False)], dtype=np.int64)
    repeats = disk_map.astype(np.int64)
    files = disk_map.copy().astype(str)
    files[1::2] = "."
    files[::2] = np.cumsum(files == ".").astype(str)[::2]
    files = np.repeat(files, repeats)
    i_dot = np.where(files == ".")[0]
    rev_files = files[files != "."][::-1]
    i_dots = np.where(files[:-1] != files[1:])[0][:-1]+1
    grp = np.split(files, i_dots)
    blanks = list(zip(i_dots[::2],np.diff(i_dots)[::2]))
    for u, c in list(zip(*np.unique(rev_files, return_counts=True)))[::-1]:
        for n, b in enumerate(blanks):
            if c <= b[1]:
                files[files==u] = '.'
                files[b[0]:b[0]+c] = [u]*c
                blanks[n] = (b[0]+c,b[1]-c)
                break
    files[files == '.'] = '0'
    files = files.astype(np.int64)
    result = np.sum(files * np.arange(len(files)))
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"Not Correct! Works with test data{part2()=}")
