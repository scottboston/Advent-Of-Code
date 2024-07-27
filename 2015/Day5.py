import aoc_utils.myconfig as utils


def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b


def part1():
    input_data = utils.get_data(year=2015, day=5)
    vowels = [*"aeiou"]
    restricted_strings = "ab cd pq xy".split()

    nice_total = 0

    for l in map(str.strip, input_data.splitlines()):
        check1 = sum(l.count(i) for i in vowels) > 2
        check2 = sum(1 for i in pairwise(l) if i[0] == i[1]) > 0
        check3 = sum(i in l for i in restricted_strings) == 0
        nice_total += check1 & check2 & check3

    return nice_total


def part2():
    input_data = utils.get_data(year=2015, day=5)
    nice_total = 0
    for l in map(str.strip, input_data.splitlines()):
        lpairs = pairwise(l)
        dd = {i: l.index("".join(i)) for i in lpairs}
        check1 = sum(l.find("".join(k), v + 2) + 1 for k, v in dd.items()) > 0
        check2 = sum(l[i] == l[i + 2] for i in range(len(l) - 2)) > 0
        nice_total += check1 & check2
    return nice_total


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
