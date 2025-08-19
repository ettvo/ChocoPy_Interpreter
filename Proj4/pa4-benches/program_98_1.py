# Returns 0-25 for characters a-z, 0 otherwise
def char_to_int(c: str) -> int:
    if c == "a":
        return 1
    elif c == "b":
        return 2
    elif c == "c":
        return 3
    elif c == "d":
        return 4
    elif c == "e":
        return 5
    elif c == "f":
        return 6
    elif c == "g":
        return 7
    elif c == "h":
        return 8
    elif c == "i":
        return 9
    elif c == "j":
        return 10
    elif c == "k":
        return 11
    elif c == "l":
        return 12
    elif c == "m":
        return 13
    elif c == "n":
        return 14
    elif c == "o":
        return 15
    elif c == "p":
        return 16
    elif c == "q":
        return 17
    elif c == "r":
        return 18
    elif c == "s":
        return 19
    elif c == "t":
        return 20
    elif c == "u":
        return 21
    elif c == "v":
        return 22
    elif c == "w":
        return 23
    elif c == "x":
        return 24
    elif c == "y":
        return 25
    elif c == "z":
        return 26
    return 0


s: str = ""
i: int = 0
n: int = 0
total: int = 0


s = input()
n = len(s)
while i < n:
    total = total + char_to_int(s[i])
    i = i + 1

print(total)
