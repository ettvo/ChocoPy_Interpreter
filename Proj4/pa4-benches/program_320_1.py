MOD:int = 10000007

def char_to_index(char:str) -> int:
    if char == "a":
        return 0
    if char == "b":
        return 1
    if char == "c":
        return 2
    if char == "d":
        return 3
    if char == "e":
        return 4
    if char == "f":
        return 5
    if char == "g":
        return 6
    if char == "h":
        return 7
    if char == "i":
        return 8
    if char == "j":
        return 9
    if char == "k":
        return 10
    if char == "l":
        return 11
    if char == "m":
        return 12
    if char == "n":
        return 13
    if char == "o":
        return 14
    if char == "p":
        return 15
    if char == "q":
        return 16
    if char == "r":
        return 17
    if char == "s":
        return 18
    if char == "t":
        return 19
    if char == "u":
        return 20
    if char == "v":
        return 21
    if char == "w":
        return 22
    if char == "x":
        return 23
    if char == "y":
        return 24
    if char == "z":
        return 25
    else:
        return 26
    

def freq_product(s:str) -> int:
    r:[int] = None
    f:int = 1
    i:int = 0
    temp:int = 0

    r = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while i < len(s):
        r[char_to_index(s[i])] = r[char_to_index(s[i])] + 1
        i = i + 1
    
    i = 0
    while i < len(r):
        f = (f * r[i]) % MOD
        i = i + 1

    return f

print(freq_product(input()))