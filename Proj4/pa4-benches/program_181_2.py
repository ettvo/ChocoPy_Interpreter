# by Avi Mehra #272fc
def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return -1

# by Avi Mehra #272fc
def str_to_int(string: str) -> int:
    result: int = 0
    i: int = 0

    while i < len(string):
        if char_to_int(string[i]) != -1:
            result = result * 10 + char_to_int(string[i])
        i = i + 1
    if string[0] == "-":
        return -result  
    else:
        return result

size: int = 0
i: int = 0
size = str_to_int(input())
while i < size:
    print(i + 1)
    i = i + 1