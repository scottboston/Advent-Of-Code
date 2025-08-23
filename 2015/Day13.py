import aoc_utils.myconfig as utils
import re
from itertools import permutations


def part1():
    input_data = utils.get_data(year=2015, day=13)
    dd = {'gain': 1, 'lose': -1}
    table = []
    info = {}

    for l in input_data.splitlines():
        pat = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)"
        g = re.findall(pat, l)[0]
        table.append(g)
        info[g[0] + ':' + g[3]] = int(dd[g[1]]) * int(g[2])

    people = set([p[0] for p in table])
    maxhap = -99_999
    for settings in permutations(people, len(people)):
        # print(settings)
        hap = sum(info[settings[i] + ':' + settings[i + 1]] for i in range(len(settings) - 1))
        hap += info[settings[0] + ':' + settings[len(settings) - 1]]
        hapr = sum(info[settings[i] + ':' + settings[i - 1]] for i in range(len(settings) - 1, 0, -1))
        hapr += info[settings[len(settings) - 1] + ':' + settings[0]]
        total_happiness = hap + hapr
        # print(f'{hap=} + {hapr=} = {hap+hapr}')
        maxhap = total_happiness if total_happiness > maxhap else maxhap
    return maxhap


if __name__ == '__main__':
    print(f'{part1()}')