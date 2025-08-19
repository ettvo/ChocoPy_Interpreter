def count(i:int):
    counter:int = 0
    useless:int = 0

    while counter <= i:
        print(counter)
        counter = counter + 1

        if counter % 128 != 0:
            useless = counter * 15102 // (counter % 128)
        useless = useless % 51259 
        useless = useless * counter

    return



def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return -1

def str_to_int(string: str) -> int:
    result: int = 0
    i: int = 0

    while i < len(string):
        if char_to_int(string[i]) != -1:
            result = result * 10 + char_to_int(string[i])
        i = i + 1

    if string[0] == "-":
        return -result
    return result
# ---------------

str_input:str = ""
i:int = 0

# Input parameter
str_input = input()
i = str_to_int(str_input)
    
count(i)