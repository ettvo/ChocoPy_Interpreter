# Compute min of a list
def list_min(l:[int]) -> int:
    i:int = 0
    curr_min:int = 0
    curr_min = l[0]
    while i < len(l):
        if l[i] < curr_min:
            curr_min = l[i]
        i = i + 1
    return curr_min

def str_to_int(string: str) -> int:
    # Credit: Alexander Goldberg on Edstem
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

input_list:[int] = None
inputs:int = 0

def collect_list(input_list:[int], num_inputs:int) -> [int]:
    next_num:int = 0
    next_str:str = ""
    while num_inputs > 0:
        next_str = input()
        next_num = str_to_int(next_str)
        input_list = input_list + [next_num]
        num_inputs = num_inputs - 1
    return input_list

input_list = []
inputs = str_to_int(input())

input_list = collect_list(input_list, inputs)
print(list_min(input_list))
