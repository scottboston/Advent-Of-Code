import aoc_utils.myconfig as utils
import numpy as np
import re


def get_data(year=2016, day=8, test=False):
    input_data = utils.get_data(year=year, day=day)
    if test:
        return ["rec 3x7", "rect 1x2", "rect 3x2"]
    return input_data.splitlines()


def part1():
    screen = np.zeros((6, 50))
    for l in get_data():
        if "rect" in l:
            c, r = re.findall(r"(\d+)x(\d+)", l)[0]
            screen[0 : int(r), 0 : int(c)] = 1
        else:
            if "column" in l:
                c, r = re.findall(r"x=(\d+) by (\d+)", l)[0]
                screen[:, int(c)] = np.roll(screen[:, int(c)], int(r))
            else:
                c, r = re.findall(r"y=(\d+) by (\d+)", l)[0]
                screen[int(c), :] = np.roll(screen[int(c), :], int(r))
    return int(np.sum(screen)), screen


def part2():
    screen = part1()[1]
    screen = np.where(screen == 1, "#", " ")
    print("Part 2:\n")
    for row in screen:
        print(" ".join(row))
    return


if __name__ == "__main__":
    print(f"{part1()[0]=}")
    part2()
