def count_odd_digits(x: str) -> int:
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i:int = 0

    # Parse digits
    while i < len(x):
        char = x[i]
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            result = result + 1
        elif char == "2":
            result = result + 1
        elif char == "4":
            result = result + 1
        elif char == "6":
            result = result + 1
        elif char == "8":
            result = result + 1
        elif char == " " or char == "\n" or char == "\t":
            return result
        elif char != "1" and char != "3" and char != "5" and char != "7" and char != "9":
            return 0 # On error
        i = i + 1
    return result
print(count_odd_digits(input()))