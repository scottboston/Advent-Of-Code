import aoc_utils.myconfig as utils
import re

input_data = utils.get_data(2025, 2)

# input_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""


def part1():
    total = 0
    for r in input_data.split(","):
        s, e = r.split("-")
        for i in range(int(s), int(e) + 1):
            a = str(i)
            if a[: len(a) // 2] == a[len(a) // 2 :]:
                total += i
    return total


def part2():
    total = 0
    for r in input_data.split(","):
        s, e = r.split("-")
        for i in range(int(s), int(e) + 1):
            pat_greedy = r"(.*)\1+"
            pat_no_greed = r"(.+?)\1+"
            repeat_no_greed = re.findall(pat_no_greed, str(i))
            repeat_greedy = re.findall(pat_greedy, str(i))
            if repeat_no_greed:
                repeat_no_greed = repeat_no_greed[0]
            if repeat_greedy:
                repeat_greedy = repeat_greedy[0]
            # print(repeat)
            try:
                if str(i).count(repeat_no_greed) * len(repeat_no_greed) == len(str(i)) or str(i).count(
                    repeat_greedy
                ) * len(repeat_greedy) == len(str(i)):
                    # print(i)
                    total += i
            except Exception as e:
                continue
    return total


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
