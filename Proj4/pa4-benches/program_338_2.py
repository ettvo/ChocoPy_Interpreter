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

#Factorial mod some prime less than sqrt of max int
def fact_mod(n: int, total: int) -> int:
    if (n <= 1):
        return total
    return fact_mod(n-1, ((n % 40151) * total) % 40151)

print(fact_mod(str_to_int(input()), 1))