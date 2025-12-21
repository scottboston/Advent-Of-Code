import aoc_utils.myconfig as utils
from itertools import chain, combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


input_text = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

input_text = utils.get_data(2025, 10).strip()


def toggle_lights(lights, buttons):
    for button in buttons:
        lights[button] = not lights[button]
    return lights


def find_min_presses(final_state, buttons):
    for presses in powerset(buttons):
        lights_on = [False] * len(final_state)
        count = 0
        for button_press in presses:
            count += 1
            lights_on = toggle_lights(lights_on, button_press)
            if lights_on == final_state:
                return count


def part1():
    sum_presses = 0
    for line in input_text.splitlines():
        lights, *buttons, energy = line.split()
        lights = lights[1:-1]
        lights = [True if bulb == "#" else False for bulb in lights]
        buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]
        sum_presses += find_min_presses(lights, buttons)
    return sum_presses

def part2():
    total_button_presses = 0
    for line in input_text.splitlines():
        lights, *buttons, energy = line.split()
        lights = lights[1:-1]
        lights = [True if bulb == "#" else False for bulb in lights]
        buttons = [list(map(int, button[1:-1].split(","))) for button in buttons]
        energy = np.array(list(map(int, energy[1:-1].split(","))))
        a = np.zeros((len(lights), len(buttons)), dtype=int)
        for i, indices in enumerate(buttons):
            for index in indices:
                a[index, i] = 1

        c = np.ones(len(buttons))
        bounds = Bounds(0, np.inf)
        constraints = LinearConstraint(a, lb=energy, ub=energy)

        integrality = np.ones(len(buttons))
        res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

        total_button_presses += sum(res.x)
    return int(total_button_presses)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")