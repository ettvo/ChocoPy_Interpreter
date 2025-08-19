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

    return result * sign

def simulate_diffusion(temps: [int], steps: int) -> [int]:
    length: int = 0
    next_temps: [int] = None
    current_temps: [int] = None
    adder: [int] = None
    time_step: int = 0
    i: int = 0

    length = len(temps)
    current_temps = temps
    adder = [0]

    while time_step < steps:
        next_temps = [0]
        i = 0
        while i < length - 1:
            next_temps = next_temps + adder
            i = i + 1

        i = 1
        while i < length - 1:
            next_temps[i] = (current_temps[i - 1] + current_temps[i] + current_temps[i + 1]) + 9781
            i = i + 1

        next_temps[0] = (current_temps[0] + current_temps[1]) + 456
        next_temps[length - 1] = (current_temps[length - 2] + current_temps[length - 1]) + 236

        current_temps = next_temps
        time_step = time_step + 1

    return current_temps

initial_temps: [int] = None
num_steps: int = 1
final_temps: [int] = None
i: int = 0

initial_temps = [100, 0, 0, 0, 25]
num_steps = str_to_int(input())
final_temps = simulate_diffusion(initial_temps, num_steps)

while (i < len(final_temps)):
    print(final_temps[i])
    i = i + 1