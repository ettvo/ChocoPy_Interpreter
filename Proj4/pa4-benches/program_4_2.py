# credit: Alex Goldberg
def str_to_int(string: str) -> int:
    # Takes in a string, which may end with a space or newline, and returns the integer value of the string
    # Integer must be between -2147483647 and 2147483647, inclusive
    # Usage: str_to_int("123")
    #        >>> 123
    # Usage: str_to_int("123\n    ")
    #        >>> 123
    # Usage: str_to_int(input()) <- -123
    #        >>> -123
    # By: Alex Goldberg
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i:int = 0

    while i < len(string):
        char = string[i]
        if char == "-":
            if not first_char:
                print("Error: Negative sign not at beginning of string")
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        elif char == " " or char == "\n" or char == "\t":
            return result * sign # Assume whitespace or newline is end of string, return result
        else:
            print("Error: Invalid character in string")
            return 0 # Error
        first_char = False
        i = i + 1
        result = result * 10 + digit

    # Compute result
    return result * sign

def pow(b: int, t: int) -> int:
    i: int = 0
    r: int = 1

    while i < t - 1:
        r = r * b
        i = i + 1

    return b * r


# https://en.wikipedia.org/wiki/Ackermann_function
def ackermann(m: int, n: int, p: int) -> int:
    if (p == 0):
        return m + n
    if (n == 0 and p == 1):
        return 0
    if (n == 0 and p == 2):
        return 1
    if (n == 0 and p >= 0 and p != 1 and not p == 2):
        return m
    else:
        return ackermann(m, ackermann(m, n - 1, p), p - 1)

inp: str = ""
m: int = 0
n: int = 0
p: int = 0

inp = input()
m = str_to_int(inp)
inp = input()
n = str_to_int(inp)
inp = input()
p = str_to_int(inp)

print(ackermann(m, n, p))