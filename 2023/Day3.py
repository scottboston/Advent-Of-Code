import aoc_utils.myconfig as utils
import re


def part1():
    input_data = utils.get_data(year=2023, day=3)
    i = input_data.split()
    num = []
    for n, l in enumerate(i):
        matches = re.finditer("\d+", l)
        for m in matches:
            s = m.start()
            e = m.end()
            mm = l[s:e]
            for lc in range(-1, 2):
                if n + lc >= 0 and n + lc < len(i):
                    s = s + 1 if s == 0 else s
                    e = e + 1 if e == len(l) else e
                    checkstr = i[n + lc][s - 1 : e + 1]
                    if isinstance(re.search("[^\d.]", checkstr), re.Match):
                        num.append(mm)
                        break
    results = sum(int(n) for n in num)
    return results


def part2():
    input_data = utils.get_data(year=2023, day=3)
    results = None
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
