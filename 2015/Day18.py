import aoc_utils.myconfig as utils
import numpy as np
from scipy.ndimage import convolve


input_data = utils.get_data(2015, 18)


def part1():
    a = np.array([[*l] for l in input_data.splitlines()])
    light = (a != ".").astype(int)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    for _ in range(100):
        light_next = convolve(light, kernel, mode="constant", cval=0.0)
        n = (light == 1) & (light_next == 2) | (light_next == 3)
        m = (light == 0) & (light_next == 3)
        light = (n + m).astype(int)
    return np.sum(light)


def part2():
    a = np.array([[*l] for l in input_data.splitlines()])
    light = (a != ".").astype(int)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    for _ in range(100):
        light_next = convolve(light, kernel, mode="constant", cval=0.0)
        n = (light == 1) & (light_next == 2) | (light_next == 3)
        m = (light == 0) & (light_next == 3)
        light = (n + m).astype(int)
        light[0, 0] = 1
        light[0, -1] = 1
        light[-1, 0] = 1
        light[-1, -1] = 1
    return np.sum(light)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
