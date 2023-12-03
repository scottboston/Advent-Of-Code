import aoc_utils.myconfig as utils
import re


def part1():
    input_data = utils.get_data(year=2023, day=3)
    i = input_data.split()
    num = 0
    for n, l in enumerate(i):
        matches = re.finditer("\d+", l)
        for m in matches:
            s = m.start()
            e = m.end()
            mm = l[s:e]
            for lc in range(-1, 2):
                if (ln := n + lc) >= 0 and ln < len(i):
                    s = s + 1 if s == 0 else s
                    e = e + 1 if e == len(l) else e
                    checkstr = i[ln][s - 1 : e + 1]
                    if isinstance(re.search("[^\d.]", checkstr), re.Match):
                        num += int(mm)
                        break
    results = num
    return results


def part2():
    input_data = utils.get_data(year=2023, day=3)
    i = input_data.split()
    num = {}
    sumkeys = {}
    for n, l in enumerate(i):
        matches = re.finditer("\d+", l)
        for m in matches:
            s = m.start()
            e = m.end()
            mm = l[s:e]
            for lc in range(-1, 2):
                if (ln := n + lc) >= 0 and ln < len(i):
                    s = s + 1 if s == 0 else s
                    e = e + 1 if e == len(l) else e
                    checkstr = i[ln][s - 1 : e + 1]
                    if isinstance(re.search("[*]", checkstr), re.Match):
                        if num.get(key := f'{ln}, {i[ln].find("*", s - 1)}'):
                            num[key] *= int(mm)
                            sumkeys[key] += 1
                        else:
                            num[key] = int(mm)
                            sumkeys[key] = 1
    results = sum(v for k, v in num.items() if sumkeys[k] == 2)
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
