import re
import aoc_utils.myconfig as utils


def part1():
    txt = """aaaaa-bbb-z-y-x-123[abxyz]
    a-b-c-d-e-f-g-h-987[abcde]
    not-a-real-room-404[oarel]
    totally-real-room-200[decoy]"""
    txt = utils.get_data(year=2016, day=4)
    input_data = txt.splitlines()
    real_room = 0
    for room in input_data:
        checksum = re.findall(r'\[(.*)\]', room)[0]
        enc_room = re.findall(r'(.*)-\d+\[', room)[0]
        room_id = re.findall(r'-(\d+)\[', room)[0]
        count_sum = list(map(lambda x: enc_room.count(x), checksum))
        print(count_sum)
        if count_sum == sorted(count_sum, reverse=True):
            if len(count_sum) == len(set(count_sum)):
                real_room += int(room_id)
            else:

    return real_room

if __name__ == '__main__':
    print(f"part1: {part1()}")