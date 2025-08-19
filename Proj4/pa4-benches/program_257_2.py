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

# solve equation ax + by + cz = 0 for integer a, b, c, x, y, z in [-range, range]
# ignore trivial solution

a: int = 0
b: int = 0
c: int = 0
range: int = 0
ix: int = 0
iy: int = 0
iz: int = 0

a = str_to_int(input())
b = str_to_int(input())
c = str_to_int(input())
range = str_to_int(input())

ix = -range
while ix <= range:
    iy = -range
    while iy <= range:
        iz = -range
        while iz <= range:
            if a * ix + b * iy + c * iz == 0 and (ix != 0 or iy != 0 or iz != 0):
                print("SOLUTION")
                print(ix)
                print(iy)
                print(iz)
            iz = iz + 1
        iy = iy + 1
    ix = ix + 1
