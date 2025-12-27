import re
import aoc_utils.myconfig as utils
from string import ascii_lowercase


def part1():
    txt = """aaaaa-bbb-z-y-x-123[abxyz]
    a-b-c-d-e-f-g-h-987[abcde]
    not-a-real-room-404[oarel]
    totally-real-room-200[decoy]"""
    txt = utils.get_data(year=2016, day=4)
    input_data = txt.splitlines()
    real_room = 0
    for room in input_data:
        checksum = re.findall(r"\[(.*)\]", room)[0]
        enc_room = re.findall(r"(.*)-\d+\[", room)[0]
        room_id = re.findall(r"-(\d+)\[", room)[0]
        count_sum = list(map(lambda x: enc_room.count(x), checksum))
        i = sorted(
            [(c, enc_room.count(c)) for c in set(sorted(enc_room.strip())) if c != "-"],
            key=lambda x: -x[1] * 100 + ord(x[0]),
        )[:5]
        real_room += int(room_id) if all(i[x][0] == checksum[x] for x in range(5)) else 0
    return real_room


def part2():
    txt = utils.get_data(year=2016, day=4)
    input_data = txt.splitlines()
    for room in input_data:
        checksum = re.findall(r"\[(.*)\]", room)[0]
        enc_room = re.findall(r"(.*)-\d+\[", room)[0]
        room_id = re.findall(r"-(\d+)\[", room)[0]
        i = sorted(
            [(c, enc_room.count(c)) for c in set(sorted(enc_room.strip())) if c != "-"],
            key=lambda x: -x[1] * 100 + ord(x[0]),
        )[:5]
        if all(i[x][0] == checksum[x] for x in range(5)):
            room = "".join(
                [
                    (ascii_lowercase[(ascii_lowercase.find(c) + int(room_id) % 26) % 26] if c != "-" else " ")
                    for c in enc_room
                ]
            )
            # print(room, room_id)
            if "northpole" in room:
                return int(room_id)


if __name__ == "__main__":
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
