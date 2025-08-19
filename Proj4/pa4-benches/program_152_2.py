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

def make_set(n: int)->[int]:
    i: int = 0
    lst: [int] = None
    lst = []
    while i < n:
        lst = lst + [i]
        i = i + 1
    return lst

def find(parent: [int], x: int)->int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: [int], x: int, y: int):
    x_root: int = 0
    y_root: int = 0

    x_root = find(parent, x)
    y_root = find(parent, y)

    if x_root != y_root:
        parent[x_root] = y_root

    
# input structure:
# n
# m
# p
# 2 * m entries
# 2 * p entries

n: int = 0
m: int = 0
m1:int = 0
m2:int = 0
i: int = 0
p: int = 0
p1:int = 0
p2: int = 0
graph: [int] = None

n = str_to_int(input()) # size of graph
m = str_to_int(input()) # how many unions we do
p = str_to_int(input()) # how many finds we do
graph = make_set(n)

while i < m:
    m1 = str_to_int(input())
    m2 =  str_to_int(input())
    union(graph, m1, m2)
    i = i + 1

i = 0

while i < p:
    p1 = str_to_int(input())
    p2 = str_to_int(input())

    if find(graph, p1) == find(graph, p2):
        print("Same parent for: ")
        print(p1)
        print(p2)
    else:
        print("Different parent for: ")
        print(p1)
        print(p2)

    i = i + 1