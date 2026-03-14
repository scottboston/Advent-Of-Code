import numpy as np
import re
import aoc_utils.myconfig as utils

input_data = """0,9 -> 5,9
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
0,9 -> 2,9
3,4 -> 1,4
"""

input_data = utils.get_data(2021, 5)

def part1():
    dd = {}
    for line in input_data.splitlines():
        y1, x1, y2, x2 = map(int, re.findall(r"-?\d+", line))
        dy = y2 - y1
        dx = x2 - x1
        if dy != 0 and dx != 0:
            continue
        cy, cx = y1, x1
        if (cy, cx) in dd:
            dd[(cy, cx)] += 1
        else:
            dd[(cy, cx)] = 1
        # print(y1, x1, y2, x2, dy, dx)
        while (cy != y2) or (cx != x2):
            cy += 1*np.sign(dy) if dy != 0 else 0
            cx += 1*np.sign(dx) if dx != 0 else 0
            # print(cy, cx)
            if (cy, cx) in dd:
                dd[(cy, cx)] += 1
            else:
                dd[(cy, cx)] = 1
    return sum(v>=2 for v in dd.values())

def part2():
    dd = {}
    for line in input_data.splitlines():
        y1, x1, y2, x2 = map(int, re.findall(r"-?\d+", line))
        dy = y2 - y1
        dx = x2 - x1

        cy, cx = y1, x1
        if (cy, cx) in dd:
            dd[(cy, cx)] += 1
        else:
            dd[(cy, cx)] = 1
        while (cy != y2) or (cx != x2):
            cy += 1 * np.sign(dy) if dy != 0 else 0
            cx += 1 * np.sign(dx) if dx != 0 else 0
            if (cy, cx) in dd:
                dd[(cy, cx)] += 1
            else:
                dd[(cy, cx)] = 1
    return sum(v >= 2 for v in dd.values())

if __name__ == "__main__":
    print(f"Part1 = {part1()}")
    print(f"Part2 = {part2()}")
