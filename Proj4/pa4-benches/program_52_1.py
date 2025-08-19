def sum(s: str, start_index: int) -> int:
    if len(s) == start_index:
        return 0

    return char_to_int(s[start_index]) + sum(s, start_index + 1)

def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return 0

inpt: str = ""
inpt = input()
print(sum(inpt, 0))