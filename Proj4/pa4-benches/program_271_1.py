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

def owen(x:[int], i:int):
    while i < len(x):
        print(x[i])
        i = i + 1

y:int = 0      
x:[int] = None
x = [3,1,4,1,5,9,2,6,5,3,5,8]
y = str_to_int(input())
owen(x, y)
