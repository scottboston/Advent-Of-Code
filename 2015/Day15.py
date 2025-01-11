from itertools import product


def part1():
    total_score = (
        lambda F, C, B, S: max(0, (F * 4 + C * 0 + B * -1 + S * 0))
        * max(0, (F * -2 + C * 5 + B * 0 + S * 0))
        * max(0, (F * 0 + C * -1 + B * 5 + S * -2))
        * max(0, (F * 0 + C * 0 + B * 0 + S * 2))
    )
    ingredients = [
        (F, C, B, S)
        for F, B, C, S in product(
            range(0, 101), range(0, 101), range(0, 101), range(0, 101)
        )
        if sum([F, B, C, S]) == 100
    ]
    recipe = max(
        ingredients,
        key=lambda x: max(0, (x[0] * 4 + x[1] * 0 + x[2] * -1 + x[3] * 0))
        * max(0, (x[0] * -2 + x[1] * 5 + x[2] * 0 + x[3] * 0))
        * max(0, (x[0] * 0 + x[1] * -1 + x[2] * 5 + x[3] * -2))
        * max(0, (x[0] * 0 + x[1] * 0 + x[2] * 0 + x[3] * 2)),
    )
    return total_score(*recipe)


def part2():
    total_score = (
        lambda F, C, B, S: max(0, (F * 4 + C * 0 + B * -1 + S * 0))
        * max(0, (F * -2 + C * 5 + B * 0 + S * 0))
        * max(0, (F * 0 + C * -1 + B * 5 + S * -2))
        * max(0, (F * 0 + C * 0 + B * 0 + S * 2))
    )
    ingredients = [
        (F, C, B, S)
        for F, B, C, S in product(
            range(0, 101), range(0, 101), range(0, 101), range(0, 101)
        )
        if sum([F, B, C, S]) == 100 and F * 5 + C * 8 + B * 6 + S * 1 == 500
    ]
    recipe = max(
        ingredients,
        key=lambda x: max(0, (x[0] * 4 + x[1] * 0 + x[2] * -1 + x[3] * 0))
        * max(0, (x[0] * -2 + x[1] * 5 + x[2] * 0 + x[3] * 0))
        * max(0, (x[0] * 0 + x[1] * -1 + x[2] * 5 + x[3] * -2))
        * max(0, (x[0] * 0 + x[1] * 0 + x[2] * 0 + x[3] * 2)),
    )
    return total_score(*recipe)


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
