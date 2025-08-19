n: int = 0
a: [int] = None
i: int = 0
j: int = 0


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
i = 0
a = []
while i < n:
    a = a + [i]
    i = i + 1

print(len(a))

i = 1
while i < n:
    j = i
    while j < n:
        a[j] = a[j] + a[i]
        j = j + i

    i = i + 1

i = 0
while i < n:
    print(a[i])
    i = i + 1
