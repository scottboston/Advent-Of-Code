import numpy as np
from itertools import combinations
import aoc_utils.myconfig as utils
import re


arr0 = np.array([[0,0,1],[0,1,1],[1,1,1]])
arr1 = np.array([[1,1,0],[0,1,1],[0,0,1]])
arr2 = np.array([[1,1,0],[0,1,1],[1,1,1]])
arr3 = np.array([[1,1,1],[1,0,1],[1,0,1]])
arr4 = np.array([[0,1,1],[0,1,1],[1,1,1]])
arr5 = np.array([[1,0,1],[1,1,1],[1,0,1]])

input_data = utils.get_data(2025, 12)

def part1():
    total = 0
    shape_area = np.array([np.sum(arr0), np.sum(arr1), np.sum(arr2), np.sum(arr3), np.sum(arr4), np.sum(arr5)])
    for l in input_data.splitlines():
        if re.match(r'\d{2}x\d{2}', l):
            region, shapes = l.split(": ")
            count_shapes = np.array(list(map(int, shapes.split(' '))))
            area_region = int(region.split('x')[0]) * int(region.split('x')[1])
            # print(area_region, (count_shapes*shape_area).sum())
            total += (area_region>=(count_shapes*shape_area).sum()).astype(int)
    return total

if __name__ == "__main__":
    print(f'Part 1: {part1()}')