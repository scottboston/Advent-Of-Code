def calc(instr):
    return (instr * 252533) % 33554393


def part1():
    n = 100_000
    instr = 20151125
    find_r = 3010
    find_c = 3019
    dd = {}
    for r in range(n):
        for c in range(r + 1):
            # print(f"{r-c+1},{c+1}")
            if r == 0 and c == 0:
                da = instr
            else:
                instr = calc(instr)
                q = instr
            if (r - c + 1) == find_r and (c + 1 == find_c):
                return instr


if __name__ == "__main__":
    print(f"part1: {part1()}")
