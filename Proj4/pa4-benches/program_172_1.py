def int_to_char(i: int) -> str:
    return "0123456789"[i]


def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if int_to_char(i) == char:
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


def fgg(s: str, n: int) -> str:
    if n == 0:
        return s
    else:
        return fgg(s, n - 1)


def fgo(o: object, n: int) -> object:
    if n == 0:
        return o
    else:
        return fgo(o, n - 1)


n: int = 0
o: object = None

print(str_to_int(fgg(input(), 10)))

while n < 192:
    n = n + 1
    o = fgo([o, n], n)
