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


def pow2(n: int) -> int:
    temp: int = 0
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = pow2(n // 2)
        return temp * temp
    else:
        temp = pow2(n // 2)
        return temp * temp * 2

def get_bit(n: int, k: int) -> int:
    return (n // pow2(k)) % 2

def xor(a: int, b: int) -> int:
    i: int = 31
    res: int = 0

    while i >= 0:
        if get_bit(a, i) != get_bit(b, i):
            res = res + pow2(i)
        i = i - 1
    return res

range: int = 0
threshold: int = 0
row: int = 0
col: int = 0

count: int = 0

range = str_to_int(input())
threshold = str_to_int(input())

row = 0
while row < range:
    col = 0
    while col < range:
        if xor(row, col) >= threshold:
            count = count + 1
        col = col + 1
    row = row + 1

print(count)
