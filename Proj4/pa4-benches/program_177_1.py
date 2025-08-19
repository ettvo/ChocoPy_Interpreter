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


def power(base:int, exp:int) -> int:
    # Calculates base**exp
    # Only supports positive exponents
    i:int = 0
    result:int = 1
    while i < exp:
        result = result * base
        i = i + 1
    return result

def swap(l: [object], i:int, j:int):
    o:object = None

    o = l[i]
    l[i] = l[j]
    l[j] = o

def permutations(k:int, l: [object]) -> int:
    # Generate permutations using Heap's algorithm:
    # https://en.wikipedia.org/wiki/Heap%27s_algorithm
    i:int = 0
    o:object = None
    count:int = 0

    if k <= 0:
        return 0

    if k == 1:
        while i < len(l):
            o = l[i]
            i = i + 1
        return 1

    # Generate permutations with k unaltered
    count = count + permutations(k - 1, l)
    while i < k - 1:
        # Swap based on parity of k
        if k % 2 == 0:
            swap(l, i, k - 1)
        else:
            swap(l, 0, k - 1)
        count = count + permutations(k-1, l)
        i = i + 1
    
    return count

def all_permutations_all_sizes(l: [object]) -> int:
    powerset_count:int = 0
    powerset_index:int = 0
    i:int = 0
    l_index:int = 0
    subset:[object] = None
    o:object = None
    count:int = 0

    powerset_count = power(2, len(l))

    while powerset_index < powerset_count:
        subset = []
        i = powerset_index
        l_index = 0
        while i > 0:
            if i % 2 == 1:
                subset = subset + [l[l_index]]
            i = i // 2
            l_index = l_index + 1
        
        count = count + permutations(len(subset), subset)

        powerset_index = powerset_index + 1

    print("Number of permutations of all sizes:")
    print(count)

    return powerset_count

def arange(start:int, end:int) -> [int]:
    # Generates list of integers from start to end, inclusive of start, exclusive of end
    result:[int] = None
    i:int = 0

    i = start
    result = []

    while i < end:
        result = result + [i]
        i = i + 1
    
    return result

zero:object = None
o_list:[object] = None
list_size:int = 0

list_size = str_to_int(input())

zero = 0

o_list = [zero] + arange(1, list_size)

all_permutations_all_sizes(o_list)