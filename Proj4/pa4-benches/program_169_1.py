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


def cube(x: int) -> int:
    square: int = 0
    result: int = 0
    i: int = 0
    square = x * x

    while i < x:
        result = result + square
        i = i + 1

    return result


def f(n: int) -> object:
    a: int = 0

    def g(i: int) -> object:
        n
        if i > 0:
            a
            h(i - 1)

    def h(i: int) -> object:
        if i > 0:
            if i % 2 == 0:
                n
                a
                g(i - 1)
            ff(i - 1)
            a

    g(n)

    return n


def ff(n: int) -> object:
    def g(i: int) -> object:
        def gg(i: int) -> object:
            if i > 0:
                n
                h(i - 1)
            n

        gg(i)
        h(i)

    def h(i: int) -> object:
        n
        if i > 0:
            f(i - 1)

    g(n)

    return n


n: int = 0
i: int = 0
o: object = None
s: str = ""

o = f(str_to_int(input()))
print(o)

s = input()
while s != "":
    n = str_to_int(s)

    i = 0
    while i < cube(n):
        if i < 4:
            print(i)
        n = n + 1
        n = n - 1
        i = i + 1

    s = input()
