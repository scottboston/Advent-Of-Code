import aoc_utils.myconfig as utils

input_data = """3-5
10-14
16-20
12-18
21-21
21-21

1
5
8
11
17
32"""

input_data = utils.get_data(2025, 5)

def part1():
    ranges= []
    foods= []
    for l in input_data.splitlines():
        if '-' in l:
            ranges.append(list(map(int, l.split('-'))))
        elif l == '':
            continue
        else:
            foods.append(int(l))
    fresh_count = 0
    for i in foods:
        fresh_count += any(i in range(fresh[0], fresh[1]+1) for fresh in ranges)

    return fresh_count

def part2():
    ranges = []
    for l in input_data.splitlines():
        if '-' in l:
            ranges.append(list(map(int, l.split('-'))))
        elif l == '':
            break
    sortedranges = sorted(ranges, key=lambda x: x[0])
    ingredients = 0
    max_seen = 0
    for r in sortedranges:
        if r[0] <= max_seen:
            ingredients += max(0, r[1] - max_seen)
            max_seen = max(r[1], max_seen)
        else:
            ingredients += r[1] - r[0] + 1
            max_seen = r[1]
    return ingredients

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')