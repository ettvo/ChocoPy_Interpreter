def str_to_int(x: str) -> int:
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i: int = 0

    # Parse digits
    while i < len(x) and x[i] != "\n":
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
            pass
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit
        i = i + 1

    # Compute result
    return result * sign

def get_int_list() -> [int]:
    i: int = 0
    string: str = ""
    ints: [int] = None

    ints = []
    string = input()
    while string != "\n":
        ints = ints + [str_to_int(string)]
        string = input()
    return ints

def swap(ints: [int], i: int, j: int):
    tmp: int = 0
    tmp = ints[i]
    ints[i] = ints[j]
    ints[j] = tmp

def sort(ints: [int]):
    i: int = 1
    j: int = 1
    while i < len(ints):
        j = i
        while j > 0 and ints[j-1] > ints[j]:
            swap(ints, j, j-1)
            j = j - 1
        i = i + 1

def main():
    ints: [int] = None
    i: int = 0

    ints = get_int_list()
    sort(ints)
    while i < len(ints):
        print(ints[i])
        i = i + 1

main()
