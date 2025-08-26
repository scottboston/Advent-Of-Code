from itertools import product
from itertools import combinations

WEAPONS = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
ARMOR = [(13, 1), (31, 2), (53, 3), (75, 4), (102, 5), (0, 0)]
RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),
    (0, 0, 0),
]

MONSTER = [8, 2, 109]


def fight(P, M):
    while True:
        M[2] -= max(P[0] - M[1], 1)
        if M[2] <= 0:
            return True
        P[2] -= max(M[0] - P[1], 1)
        if P[2] <= 0:
            return False


def part1():
    player_combos = product(*[WEAPONS], *[ARMOR], *[RINGS], *[RINGS])
    players_cost = [
        (
            p[0][1] + p[2][1] + p[3][1],
            p[1][1] + p[2][2] + p[3][2],
            100,
            p[0][0] + p[1][0] + p[2][0] + p[3][0],
        )
        for p in player_combos
    ]
    winning_players = [
        player for player in players_cost if fight(list(player[:3]), list(MONSTER))
    ]
    return min(winning_players, key=lambda x: x[3])[3]


def part2():
    player_combos = []
    for w, a in product(WEAPONS, ARMOR):
        for r1, r2 in combinations(RINGS, 2):
            player_combos.append((w, a, r1, r2))

    players_cost = [
        (
            p[0][1] + p[2][1] + p[3][1],
            p[1][1] + p[2][2] + p[3][2],
            100,
            p[0][0] + p[1][0] + p[2][0] + p[3][0],
        )
        for p in player_combos
    ]
    losing_players = [
        player
        for player in sorted(players_cost, key=lambda x: -x[3])
        if not fight(list(player[:3]), list(MONSTER))
    ]
    return max(losing_players, key=lambda x: x[3])[3]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
