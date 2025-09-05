import aoc_utils.myconfig as utils
from string import ascii_lowercase

def increment_password(password):
    chars = list(password)
    i = len(chars) - 1
    while i >= 0:
        if chars[i] == 'z':
            chars[i] = 'a'
            i -= 1
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            break
    return ''.join(chars)

def is_valid_password(password):
    # Check for forbidden letters
    if any(c in password for c in 'iol'):
        return False
    
    # Check for increasing straight of 3 letters
    has_straight = any(ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2 
                      for i in range(len(password) - 2))
    if not has_straight:
        return False
    
    # Check for at least two different pairs
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            pairs.add(password[i])
            i += 2  # Skip next char to avoid overlapping
        else:
            i += 1
    
    return len(pairs) >= 2

def part1():
    password = "hepxcrrq"
    
    while True:
        password = increment_password(password)
        if is_valid_password(password):
            return password

def part2():
    password = part1()
    
    while True:
        password = increment_password(password)
        if is_valid_password(password):
            return password


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
