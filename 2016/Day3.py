import aoc_utils.myconfig as utils
from itertools import permutations


input_data = utils.get_data(year=2016, day=3)


def part1():
    total = 0
    for line in input_data.splitlines():
        sides = list(map(int, line.split()))
        total += int(all(sides[i]+sides[j] > sides[k] for i, j, k in permutations(range(3), 3)))
    return total

def part2():
    rect = []
    total = 0
    for line in input_data.splitlines():
        rect.append(list(map(int, line.split())))
    for column in range(3):
        for i in range(0,len(rect),3):
            total += int(all(rect[i][column] + rect[j][column] > rect[k][column] for i, j, k in permutations(range(i,i+3), 3)))
    return total

if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")