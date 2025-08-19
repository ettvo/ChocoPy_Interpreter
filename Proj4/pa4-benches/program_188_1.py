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

def dependency():
    x : int = 0
    i : int = 0
    c : int = 0
    a : int = 4
    b : int = 5
    i = 0
    i = 1
    i = 2
    i = 3
    i = 4
    i = 0
    i = 1
    i = 2
    i = 3
    i = 4
    i = 0
    i = 1
    i = 2
    i = 3
    i = 4
    i = 0
    i = 1
    i = 2
    i = 3
    i = 4 + 2

    i = i + i * 2 + 1

    print("Despite this long thing, I will optimize them out")

    print(c)

    c = i + 2
    a = c + 15 + a
    b = c + 15 + a

    print(b)
    print(c)

i : int = 0

n : int = 0

print("Gimme an input")
n = str_to_int(input())
while i <= n:
    dependency()
    i = i + 1


