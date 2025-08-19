# The following to_int functions are a modified version of the code posted by Avi Mehra
# to edstem: https://edstem.org/us/courses/54579/discussion/4731834?comment=11030750
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
    if len(string) == 0:
        return 0
    if string[0] == "-":
        i = 1
    while i < len(string):
        if char_to_int(string[i]) != -1:
            result = result * 10 + char_to_int(string[i])
            i = i + 1
        else:
            i = len(string)

    if string[0] == "-":
        return -result
    return result

x: int = 0
def increment_dead(n: int) -> int:
    tot: int = 0
    dead: int = 0
    while n >= 0:
        n = n-1
        dead = increment_dead(n)
        tot = tot + 1
    return tot

print(increment_dead(str_to_int(input())))