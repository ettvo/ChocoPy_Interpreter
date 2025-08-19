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

def slice(list: [int], start: int, end: int) -> [int]:
    output:[int] = None
    i: int = 0
    if start >= end:
        output = []
        return output
    else:
        output = []
        i = start
        while i < end:
            output = output + [list[i]]
            i = i + 1
        return output
    

def merge_sort(lst: [int]) -> [int]:
    mid: int = 0
    left: [int] = None
    right:  [int] = None
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(slice(lst, 0, mid))
    right = merge_sort(slice(lst, mid, len(lst)))
    return merge(left, right)

def merge(left: [int], right: [int]) -> [int]:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    if left[0] <= right[0]:
        # return [left[0]] + merge(left[1:], right)
        return [left[0]] + merge(slice(left, 1, len(left)), right)

    return [right[0]] + merge(left, slice(right, 1, len(right)))
    # return [right[0]] + merge(left, right[1:])


n: int = 0
s:str = ""
i:int = 0
j:int = 0
l: [int] = None


n = str_to_int(input())
l = []

while i < n:
    l = l + [str_to_int(input())]
    i = i + 1

i = 0
print("BELOW IS INPUT")
while i < n:
    print(l[i])
    i = i + 1

# print(s)

l = merge_sort(l)

print("BELOW IS SORTED OUTPUT")
while j < n:
    print(l[j])
    j = j + 1

# print(s)



