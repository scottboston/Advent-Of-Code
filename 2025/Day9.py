from shapely import Polygon

import aoc_utils.myconfig as utils
from itertools import combinations
from shapely import Polygon, Point


input_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

input_data = utils.get_data(2025, 9)

def rectangle_area(c1, c3):
    l = abs(c1[0] - c3[0]) + 1
    w = abs(c1[1] - c3[1]) + 1
    return l * w

def four_corners(c1, c3):
    c2 = (c1[0], c3[1])
    c4 = (c3[0], c1[1])
    return [c1, c2, c3, c4]

def part1():
    corners = [tuple(map(int, l.split(','))) for l in input_data.splitlines()]
    rectangles = combinations(corners, 2)
    max_area = max(rectangles, key=lambda r: rectangle_area(r[0], r[1]))
    return max_area, rectangle_area(*max_area)


def part2():
    corners = [tuple(map(int, l.split(','))) for l in input_data.splitlines()]
    polygon = Polygon([Point(c[0], c[1]) for c in corners])
    rectangles = combinations(corners, 2)
    inside_rectangles = []
    for corner1, corner3 in rectangles:
        if polygon.contains(Polygon([Point(c) for c in four_corners(corner1, corner3)])):
            inside_rectangles.append((corner1, corner3))
    max_area = max(inside_rectangles, key=lambda r: rectangle_area(r[0], r[1]))
    return max_area, rectangle_area(*max_area)

if __name__ == '__main__':
    print(f'Part 1: {part1()[1]}')
    print(f'Part 2: {part2()[1]}')