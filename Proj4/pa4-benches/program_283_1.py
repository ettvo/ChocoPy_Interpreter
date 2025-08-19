# unroll loops test

n: int = 0
i: int = 0
k: int = 0


def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return -1


def str_to_int(string: str) -> int:
    result: int = 0
    i: int = 0

    while i < len(string):
        if char_to_int(string[i]) != -1:
            result = result * 10 + char_to_int(string[i])
        i = i + 1

    if string[0] == "-":
        return -result
    return result


n = str_to_int(input())
k = n
while k > 0:
    k = k // 2

while i < 100:
    n = ((n + 69) // 324123 + 420) + 69 + 420 - n + i * 69
    print(n)
    i = i + 1
