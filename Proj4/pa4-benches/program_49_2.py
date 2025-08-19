# Adds up all the digits of the given string and returns the sum.
def sum(s: str) -> int:
    ret: int = 0
    index: int = 0

    while (index < len(s)):
        ret = ret + char_to_int(s[index])
        index = index + 1

    return ret

def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return 0

inpt: str = ""
inpt = input()

print(sum(inpt))