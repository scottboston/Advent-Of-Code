import aoc_utils.myconfig as utils
from functools import cache, lru_cache
from tqdm import tqdm

input_data = """125 17"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 11)


def part1():
    l = get_input_data(False).split()

    for _ in tqdm(range(25)):
        l = (stone_blink(int(e)) for e in l)
        l = sum(l, [])
        # print(f'{l=}')

    result = len(l)
    print(stone_blink.cache_info())
    return result


def part2():
    l = get_input_data(False).split()
    sum_len = sum(stone_blink_len(int(e), 75) for e in l)
    result = sum_len
    return result


@lru_cache(maxsize=None)
def stone_blink(stone_number):
    print(f"Cache miss: {stone_number}")
    if stone_number == 0:
        return [1]
    elif len(c := (str(stone_number))) % 2 == 0:
        return [int(c[len(c) // 2 :]), int(c[: len(c) // 2])]
    else:
        return [stone_number * 2024]


@lru_cache(maxsize=None)
def stone_blink_len(stone_number, blink_len):
    if blink_len == 0:
        return 1
    elif stone_number == 0:
        return stone_blink_len(1, blink_len - 1)
    elif len(c := (str(stone_number))) % 2 == 0:
        return stone_blink_len(int(c[len(c) // 2 :]), blink_len - 1) + stone_blink_len(
            int(c[: len(c) // 2]), blink_len - 1
        )
    else:
        return stone_blink_len(stone_number * 2024, blink_len - 1)


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
