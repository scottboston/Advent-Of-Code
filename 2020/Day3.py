import aoc_utils.myconfig as utils
import numpy as np

input_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

input_data = utils.get_data(year=2020, day=3)

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def part1():
    arr = np.array([[*l] for l in input_data.splitlines()])
    arr = arr == "#"
    depth, width = arr.shape
    return sum(arr[i, (i * 3) % int(width)] for i in range(depth))


def part2():
    arr = np.array([[*l] for l in input_data.splitlines()])
    arr = arr == "#"
    depth, width = arr.shape
    return np.prod(
        [
            sum(arr[i, (n * x) % int(width)] for n, i in enumerate(range(0, depth, y)))
            for x, y in SLOPES
        ]
    )


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
