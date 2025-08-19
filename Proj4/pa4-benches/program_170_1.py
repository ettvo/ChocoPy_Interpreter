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


def fgg(n: int) -> int:
    i: int = 0
    result: int = 1

    while i < n * n * n * n:
        i = i + 1
        result = result * 2
        result = result % 3

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


s: str = ""
o: object = None

o = f(5)
print(o)

s = input()

while len(s) > 0:
    print(fgg(str_to_int(s)))
    s = input()
