int_input: int = 0

# https://edstem.org/us/courses/54579/discussion/4731834?comment=11030750 for char_to_int and str_to_int

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


def factorial(n: int) -> int:
    result: int = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result

print(factorial(str_to_int(input())))
