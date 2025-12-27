import hashlib


def part1(seed="abc"):
    password_list = []
    i = 0
    found = 0
    while found < 8:
        h = hashlib.md5(seed.encode("utf-8") + str(i).encode("utf-8")).hexdigest()
        if h.startswith("00000"):
            found += 1
            password_list.append(h)
        i += 1
    return "".join([c[5] for c in password_list])


def part2(seed="abc"):
    i = 0
    password = [" "] * 8
    while " " in password:
        h = hashlib.md5(seed.encode("utf-8") + str(i).encode("utf-8")).hexdigest()
        if h.startswith("00000"):
            try:
                if int(h[5]) < 8:
                    password[int(h[5])] = (
                        h[6] if password[int(h[5])] == " " else password[int(h[5])]
                    )
            except Exception as e:
                pass
        i += 1
    return "".join(password)


if __name__ == "__main__":
    print(part1("wtnhxymk"))
    print(part2("wtnhxymk"))
