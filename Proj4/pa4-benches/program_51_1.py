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

def quadradic(size: int, x: str) -> int:
    
    def yo(s: str) -> int:
        ret: int = 0
        index: int = 0

        while (index < len(s)):
            ret = ret + char_to_int(s[index])
            index = index + 1

        return ret
    
    r: int = 0
    i: int = 0

    while (i < size):
        r = r + yo(x)
        i = i + 1
    
    return r

size: str = ""
number: str = ""
size = input()
number = input()
print(quadradic(str_to_int(size), number))