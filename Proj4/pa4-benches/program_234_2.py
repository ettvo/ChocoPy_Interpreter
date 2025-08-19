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


def get_list() -> [int]:
    n:int = 0
    i:int = 0
    t:int = 0

    ls:[int] = None
    ls = []

    n = str_to_int(input())
    while i < n:
        t = str_to_int(input())
        ls = ls + [t]
        i = i + 1

    return ls


def print_list(l:[int]) -> object:
    i:int = 0
    while i < len(l):
        print(l[i])
        i = i + 1


def max(a:int, b:int) -> int:
    if a >= b:
        return a
    else:
        return b

def copy_list(a:[int]) -> [int]:
    l:[int] = None
    i:int = 0

    l = []
    while i < len(a):
        l = l + [a[i]]
        i = i + 1
    return l

def merge(left:[int], right:[int]) -> [int]:
    result:[int] = None
    Lm:int = 0
    Rm:int = 0
    L:int = 0
    R:int = 0

    result = []
    Lm = len(left)
    Rm = len(right)

    while (L < Lm) and (R < Rm):
        if left[L] <= right[R]:
            result = result + [left[L]]
            L = L + 1
        else:
            result = result + [right[R]]
            R = R + 1

    while L < Lm:
        result = result + [left[L]]
        L = L + 1

    while R < Rm:
        result = result + [right[R]]
        R = R + 1

    return result

def merge_sort(m:[int]) -> [int]:
    i:int = 0
    j:int = 0
    left:[int] = None
    right:[int] = None

    left = []
    right = []

    if len(m) == 0:
        return []
    elif len(m) == 1:
        return [m[0]]

    while i < len(m):
        if i < (len(m) // 2):
            left = left + [m[i]]
        else:
            right = right + [m[i]]
        i = i + 1

    left = merge_sort(copy_list(left))
    right = merge_sort(copy_list(right))

    return merge(left, right)

ls:[int] = None
ls = get_list()
# print_list(ls)
ls = merge_sort(ls)
print_list(ls)
