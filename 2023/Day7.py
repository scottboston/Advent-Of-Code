import aoc_utils.myconfig as utils
import pandas as pd
from io import StringIO
from collections import Counter
import numpy as np


def rank_hand(cards):
    cards = sorted(cards)
    c = Counter(cards)
    # print(f'{c} {len(c.keys())=} {max(c.values())=}')
    if cards[0] == cards[-1]:
        return 6  # Five of a Kind
    elif (cards[0] == cards[3]) | (cards[1] == cards[-1]):
        return 5  # Four of a kind
    elif len(c) == 2:
        return 4  # Full House
    elif (len(c.keys()) == 3) and (max(c.values()) == 3):
        return 3  # Three of a kind
    elif (len(c.keys()) == 3) and max(c.values()) == 2:
        return 2  # Two Pair
    elif max(c.values()) == 2:
        return 1  # One Pair
    else:
        return 0  # High card


def rank_hand_j_wild(cards):
    cards = sorted(cards)
    c = Counter(cards)
    print(f"{c=}")
    try:
        js = c.pop("J")
    except KeyError:
        js = 0
    print(f"{js=} {c=}")
    if cards[0] == cards[-1] or len(c) == 1:
        print("five")
        return 6  # Five of a Kind
    elif (cards[0] == cards[3]) | (cards[1] == cards[-1]):
        print("four")
        return 5 + js  # Four of a kind
    elif len(c) == 2 & sum(c.values()) == 5:
        print("full")
        return 4 + js  # Full House
    elif (len(c.keys()) == 3) and (max(c.values()) == 3):
        print("three")
        return 3 + js  # Three of a kind
    elif (len(c.keys()) == 3) and max(c.values()) == 2 and sum(c.values()) == 5:
        print("two")
        return 2 + js * 2  # Two Pair
    elif max(c.values()) == 2:
        print("one")
        return 1 + js * 2  # One Pair
    elif js > 1:
        return 1 + js  # High card
    else:
        return 0 + js


def part1():
    card = "23456789TJQKA"
    mt = str.maketrans(card, "ABCDEFGHIJKLM")
    input_data = utils.get_data(year=2023, day=7)
    input_text = input_data.split("\n")[:-1]
    arr = np.array(list(map(str.split, input_text)))
    c = arr[:, 0]
    idx = arr[:, 1]
    df = pd.DataFrame(c, index=idx)
    df["rank_hand"] = df[0].map(rank_hand)
    df["sortkey"] = df[0].map(lambda x: x.translate(mt)).sort_values()
    dfs = df.sort_values(["rank_hand", "sortkey"])
    results = sum(dfs.index.astype(int) * np.arange(1, dfs.shape[0] + 1))
    return results


def part2():
    card = "J23456789TQKA"
    mt = str.maketrans(card, "ABCDEFGHIJKLM")
    input_data = utils.get_data(year=2023, day=7)
    input_text = input_data.split("\n")[:-1]
    arr = np.array(list(map(str.split, input_text)))
    c = arr[:, 0]
    idx = arr[:, 1]
    df = pd.DataFrame(c, index=idx)
    df["rank_hand"] = df[0].map(rank_hand_j_wild)
    df["sortkey"] = df[0].map(lambda x: x.translate(mt)).sort_values()
    dfs = df.sort_values(["rank_hand", "sortkey"])
    results = sum(dfs.index.astype(int) * np.arange(1, dfs.shape[0] + 1))
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
