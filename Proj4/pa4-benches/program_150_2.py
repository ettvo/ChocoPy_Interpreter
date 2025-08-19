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

def factorial(n: int)->int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def div_three_or_five(n: int) -> [int]:
    multiples: [int] = None
    i:int = 0
    multiples = []

    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            multiples = multiples + [i]
        i = i + 1
    return multiples


n: int = 0
i: int = 0
lst: [int] = None


n = str_to_int(input())
n = factorial(n)
lst = div_three_or_five(n)

print("Numbers less than n!, disivible by 3 or 5 are:")
while i < len(lst):
    print(lst[i])
    i = i + 1
