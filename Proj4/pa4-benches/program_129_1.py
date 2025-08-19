# store integers in list and print back out, each int should be on a new line to be parsed correctly
def str_to_int(x: str) -> int:
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
        elif char == "\n":
            return result * sign
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit
        i = i + 1

    # Compute result
    return result * sign

s:str = ""
_list:[int] = None
i: int = 0
a: int = 0
append_list: [int] = None

_list = []
s = input()
while len(s) > 0:
    a = str_to_int(s)
    append_list = [a]
    _list = _list + append_list
    s = input()

while i < len(_list):
    print(_list[i])
    i = i + 1

