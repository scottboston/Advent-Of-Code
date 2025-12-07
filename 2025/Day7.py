import aoc_utils.myconfig as utils
import numpy as np
from collections import defaultdict

input_data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input_data = utils.get_data(2025, 7)


def part1(step=2):
    arr = np.array([[*l] for l in input_data.splitlines()])
    sr, sc = np.where((arr == "^"))
    missed = 0
    for s in zip(sr, sc):
        try:
            check_r = s[0] - step
            check_c_left = s[1] - 1
            check_c_right = s[1] + 1
            min_r = max(
                (arr[: s[0], s[1]] != "^")[::-1].cumsum()
                * (arr[: s[0], s[1]] != "^")[::-1].cumprod()
            )
            if (
                check_r >= 0
                and all(arr[s[0] : s[0] - min_r : -1, check_c_left] == ".")
                and all(arr[s[0] : s[0] - min_r : -1, check_c_right] == ".")
            ):
                missed += 1
        except Exception as e:
            continue
    return len(sr) - missed + 1


def part2(step=2):
    arr = np.array([[*l] for l in input_data.splitlines()])
    sr, sc = np.where((arr == "^"))
    l = defaultdict(int)
    l[sc[0]] = 1
    for s in zip(sr, sc):
        check_c_left = s[1] - 1
        check_c_right = s[1] + 1
        l[check_c_left] += l[s[1]]
        l[check_c_right] += l[s[1]]
        l[s[1]] = 0
    return sum(v for k, v in l.items())


if __name__ == "__main__":
    # print(f'Part 1: {part1()}')
    print(f"Part 2: {part2()}")
