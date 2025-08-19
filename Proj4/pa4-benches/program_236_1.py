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

def acc_min(s:int, l:[int]) -> [int]:
    result: [int] = None
    m:int = 0
    m_i:int = 0
    i:int = 0

    result = [0, 0]

    i = s
    # m = l[s] #inf
    m = 10000000
    while i < len(l):
        if m > l[i]:
            m = l[i]
            m_i = i
        i = i + 1

    result[0] = m_i
    result[1] = m
    return result

def selection_sort(s:int, l:[int]) -> object:
    m:[int] = None
    first: int = 0
    tmp: int = 0

    if (len(l) - s) == 1:
        return

    m = acc_min(s, l)

    first = l[s]
    l[s] = l[m[0]]
    l[m[0]] = first

    return selection_sort(s+1, l)

def binary_search(l:[int], T:int) -> int:
    L:int = 0
    R:int = 0
    m:int = 0

    R = len(l) - 1
    selection_sort(0, l)
    while L <= R:
        m = (L + R) // 2
        if l[m] < T:
            L = m + 1
        elif l[m] > T:
            R = m - 1
        else:
            return m
    return -1

def remove_first(l:[int]) -> [int]:
    n:[int] = None
    i:int = 1
    n = []
    while i < len(l):
        n = n + [l[i]]
        i = i + 1
    return n

ls:[int] = None
first:int = 0
r:int = 0

ls = get_list()
first = ls[0]
ls = remove_first(ls)
print(first)

r = binary_search(ls, first)
print(r)
# print(ls[r])
