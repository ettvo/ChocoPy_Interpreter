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


def fib(n: int) -> int:
    fib_prev: int = 0
    fib_current: int = 1
    count: int = 1
    fib_next: int = 0

    if n <= 1:
        return n

    while count < n:
        fib_next = fib_prev + fib_current
        fib_prev = fib_current
        fib_current = fib_next
        count = count +  1

    return fib_current




def factorial(n: int) -> int:
    result: int = 1
    if n < 0:
        return 0   # Factorial is not defined for negative numbers
    elif n == 0:
        return 1  # Base case: 0! = 1
    else:

        while n > 0:
            result = result * n
            n = n - 1
        return result



def collatz(n: int) -> int:
    steps: int = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps = steps + 1

    return steps

print(collatz(factorial(fib(str_to_int(input())))))
