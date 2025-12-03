import re

adding = {(0, 'R') : -1 + 0j,
          (0, 'L') : 1 + 0j,
          (1, 'R') : 0 - 1j,
          (1, 'L') : 0 + 1j,
          (2, 'R') : -1 + 0j,
          (2, 'L') : 1 + 0j,
          (3, 'R') : 0 - 1j,
          (3, 'L') : 0 + 1j,}

def part1():
    s = 0 + 0j
    input_data = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"
    heading = 0
    turns = 1
    for steps in input_data.split(', '):
        turn = steps[0]
        s += int(re.findall(r'\d+', steps)[0]) * adding[(heading, turn)]
        heading = (heading + 1)%4
        print(s)
    return abs(s.real) + abs(s.imag)

if __name__ == '__main__':
    print(f"part1: {part1()}")
