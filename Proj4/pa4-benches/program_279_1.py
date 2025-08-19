# from Avi Mehra! <3
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

def exp(a:int, n:int) -> int:
    if n == 0:
        return 1
    else:
        return a * exp(a, n-1)
    
n:int = 0
i:int = 0
total:int = 0

n = str_to_int(input())

while i < n:
    total = total + 1
    i = i + 1
    i = i - 1
    i = i + 1
    i = i - 1
    i = i + 1

print(total)