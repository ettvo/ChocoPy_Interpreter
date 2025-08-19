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
            return -1 # Error
        first_char = False
        i = i + 1
        result = result * 10 + digit

    # Compute result
    return result * sign

def power_mod(base:int, exp:int, mod:int) -> int:
    # Calculates base**exp mod mod
    # This is inefficient
    i:int = 0
    result:int = 1
    base = base % mod
    while i < exp:
        result = (result * base) % mod
        i = i + 1
    return result

powers_table:[[int]] = None
powers_to_precompute:[int] = None
powers_row:[int] = None

max_base:int = 17
precomputed_mod:int = 11
powers_per_base:int = 17


choice_string:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bad_hash:[str] = None
base:int = 0
i:int = 0
j:int = 0
result:int = 0
s:str = ""
mod:int = 0
value:int = 0
operation:str = ""
iterations:int = 0
iteration_index:int = 0
power_tmp:int = 0
result_sum:int = 0

powers_table = []

while base <= max_base:
    powers_row = []
    i = int()
    while i <= powers_per_base:
        powers_row = powers_row + [power_mod(base, i, precomputed_mod)]
        i = i + 1
    powers_table = powers_table + [powers_row]
    base = base + 1

i = int()
while i < len(powers_table):
    j = int()
    while j < len(powers_table[i]):
        print(powers_table[i][j])
        j = j + 1
    print("_________")
    i = i + 1


iterations = str_to_int(input())
mod = str_to_int(input())
operation = input()
value = str_to_int(input())

while iteration_index < iterations:
    i = int()
    bad_hash = []
    result_sum = int()
    while i < len(powers_table):
        j = int()
        while j < len(powers_table[i]):
            if mod == precomputed_mod:
                power_tmp = powers_table[i][j]
            else:
                power_tmp = power_mod(i, j, mod)

            if operation == "+\n":
                result = power_tmp + (value % mod)
            elif operation == "-\n":
                result = power_tmp - (value % mod)
            elif operation == "*\n":
                result = power_tmp * (value % mod)
            elif operation == "//\n":
                result = power_tmp // (value % mod)
            elif operation == "%\n":
                result = power_tmp % (value % mod)
            elif operation == "==\n":
                if power_tmp == value:
                    result = 1
                else:
                    result = 0
            else:
                print("Bad operation")

            result = result % mod
            bad_hash = [choice_string[(result // 2) % len(choice_string)]]
            while len(bad_hash) > 64 and bad_hash[len(bad_hash) - 1] != "A":
                bad_hash = bad_hash + ["C"]

            result_sum = result_sum + result

            j = j + 1
        i = i + 1
    iteration_index = iteration_index + 1

print(result_sum)