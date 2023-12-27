import aoc_utils.myconfig as utils
import re
import numpy as np
import pandas as pd
from functools import partial


def part1():
    input_data = utils.get_data(year=2015, day=14)

    def get_distance(t, flight_dur, flight_speed, rest_dur):
        completed = (t // (flight_dur + rest_dur) + 1) * flight_dur * flight_speed if t % (
                    flight_dur + rest_dur) > flight_dur else t // (flight_dur + rest_dur) * flight_dur * flight_speed
        flying_now = t % (flight_dur + rest_dur) * flight_speed if t % (flight_dur + rest_dur) < flight_dur else 0
        return completed + flying_now

    max_dist = 0
    for deer in input_data.splitlines():
        t = 2503
        flight_speed, flight_dur, rest_dur = map(int, re.findall('\d+', deer))
        dist = get_distance(t, flight_dur, flight_speed, rest_dur)
        max_dist = dist if dist > max_dist else max_dist
    results = max_dist
    return results

def part2():
    input_data = utils.get_data(year=2015, day=14)
    def get_distance(t, flight_speed, flight_dur, rest_dur):
        completed = (t // (flight_dur + rest_dur) + 1) * flight_dur * flight_speed if t % (
                    flight_dur + rest_dur) >= flight_dur else t // (flight_dur + rest_dur) * flight_dur * flight_speed
        flying_now = t % (flight_dur + rest_dur) * flight_speed if t % (flight_dur + rest_dur) < flight_dur else 0
        return completed + flying_now

    find_all = partial(re.findall, '\d+')

    s = []
    for i in range(1, 2_504):
        d=np.array([get_distance(i, *map(int, e)) for n, e in enumerate(map(find_all, input_data.splitlines()))])
        s.extend(np.where(d == max(d))[0].tolist())

    results = pd.Series(s).value_counts().max()
    return results


if __name__ == '__main__':
    print(f'{part1()=}')
    print(f'{part2()=}')