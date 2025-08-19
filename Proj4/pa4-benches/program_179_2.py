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

g_int:int = 0
g_list:[object] = None
o:object = None

def a(a_times:int) -> int:
    a_int:int = 0
    a_str:str = "I'm a:"

    def b(b_times:int) -> int:
        b_str:str = "This is b:"

        def c(c_times:int) -> int:
            c_str:str = "Here is c:"
            i:int = 0

            print(c_str)
            while i < len(g_list):
                g_list[i] = b_times
                i = i + 1

            return len(g_list)

        c(b_times)
        print(b_str)
        return a_int + b_times

    if a_times <= 0:
        print(a_str)
        return a_int
    
    a_int = a_times * 2

    b(a_times)
    a(a_times - 1)

    print(a_int)
    print(a_str)

    return a_times - a_int * g_int

a_times:int = 0

a_times = str_to_int(input())

o = "List start"
g_list = [o, o, o, o, o]


print(a(a_times))
print(len(g_list))
print(g_list[2])
print(g_int)