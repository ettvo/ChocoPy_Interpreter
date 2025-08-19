def vowel_count(x: str) -> int:
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
        elif char == "a":
            result = result + 1
        elif char == "e":
            result = result + 1
        elif char == "i":
            result = result + 1
        elif char == "o":
            result = result + 1
        elif char == "u":
            result = result + 1
        elif char == " " or char == "\n" or char == "\t":
            return result
        i = i + 1
    return result
print(vowel_count(input()))
