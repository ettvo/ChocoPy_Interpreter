def str_to_int(x: str) -> int:
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i: int = 0

    # Parse digits
    while i < len(x) and x[i] != "\n":
        char = x[i]
        if char == "-":
            if not first_char:
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
        elif char == "\n":
            pass
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit
        i = i + 1

    # Compute result
    return result * sign

def compute_with_lists(x: int) -> int:
    ones: [int] = None

    def appender():
        nonlocal ones
        j : int = 0
        while j < x:
            ones = ones + [1]
            j = j + 1

    ones = []

    while x > 0:
        appender()
        x = x - 1

    return len(ones)


def main():
    x: int = 0
    x = str_to_int(input())
    print(compute_with_lists(x))

main()

