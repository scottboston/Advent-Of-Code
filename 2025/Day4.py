import aoc_utils.myconfig as utils
import numpy as np
from scipy.ndimage import convolve

input_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

input_data = utils.get_data(2025, 4)

def part1():
    data = np.array([[*l] for l in input_data.splitlines()])
    rolls = (data == '@').astype(int)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    roll_neighbors = convolve(rolls, kernel, mode="constant", cval=0.0)
    accessible = np.sum((roll_neighbors<4)&(data=='@'))
    return accessible

def part2():
    data = np.array([[*l] for l in input_data.splitlines()])
    rolls = (data == '@').astype(int)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    removed_count = 0
    while True:
        roll_neighbors = convolve(rolls, kernel, mode="constant", cval=0.0)
        accessible = np.sum((roll_neighbors < 4) & rolls.astype(bool))
        if not accessible:
            break
        removed = ~(roll_neighbors<4)&rolls.astype(bool)
        rolls = removed.astype(int)
        removed_count += accessible
    return removed_count

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')