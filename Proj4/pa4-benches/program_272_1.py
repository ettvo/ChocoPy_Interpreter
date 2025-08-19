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

def owen(x:[str], i:int):
    while i < len(x):
        if i % 2 == 0:
            print(x[i])
        i = i + 1
        
x:[str] = None
y:int = 0
x = ["a","b","c","d", "e", "f"]
y = str_to_int(input())
owen(x, y)
