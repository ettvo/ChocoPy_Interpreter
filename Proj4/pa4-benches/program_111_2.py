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


def foo(x:int) -> int:
    pos:int = 0
    neg:int = 0
    while True:
        pos = pos + 1
        neg = neg - 1
        if x == pos or x == neg:
            print(x + 1)
            return x + 1
       
    return 0









x:int = 0
x = str_to_int(input())
foo(x)