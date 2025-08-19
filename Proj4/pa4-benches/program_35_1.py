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

a:[int] = None
b:[int] = None

c:int = 0
d:int = 0
e:int = 0
f:int = 0

i:int = 0
j:int = 0
k:int = 0

c = str_to_int(input())
d = str_to_int(input())
e = str_to_int(input())
f = str_to_int(input())
c = c + e
d = d
a = []
b = []

while i <= c:
    a = a + [i]
    print(a[i])
    while j <= d:
        b = b + [j]
        print(b[i] + a[i])
        j = j + 1

    i = i + 1
    j = 0

while k < c and k < d:
    print(a[k] == b[k])
    k = k + 1



