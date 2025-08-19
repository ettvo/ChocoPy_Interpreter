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

def pow(base:int, exp:int) -> int:
    result:int = 1
    i:int = 0
    while i < exp:
        result = result * base
        i = i + 1
    return result

a:[int] = None
b:[int] = None
i: int = 0
j: int = 0
k: int = 0
l: int = 0

a = [1]
b = [1]
k = str_to_int(input())

# note that a and b have length 2^k.
while (i < k):
    a = a + a
    b = b + b
    i = i + 1


i = 0
l = pow(2, k)

# loop interchange
while (i < 10):
    while (j < l):
        a[j] = a[j] + b[j] + j
        j = j + 1
    i = i + 1

print(a[l - 1])