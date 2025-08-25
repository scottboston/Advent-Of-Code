import aoc_utils.myconfig as utils
from functools import lru_cache
import math

def find_factors(num):
    factors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return sorted(list(factors))

def part1():
    number = 500_000
    max_present_seen = 0
    while True:
        all_factors = find_factors(number)
        presents = sum(f*10 for f in all_factors)
        if presents > max_present_seen:
            max_present_seen = presents
            print(max_present_seen, number)
            if presents >= 36_000_000:
                return number
        number += 1

def part2():
    number = 10
    max_present_seen = 0
    while True:
        all_factors = find_factors(number)
        presents = sum(f*11. for f in all_factors if number/f < 50)
        if presents > max_present_seen:
            max_present_seen = presents
            print(max_present_seen, number)
            if presents >= 36_000_000:
                return number
        number += 1

if __name__ == '__main__':
    # print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
