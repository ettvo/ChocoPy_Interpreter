# From Avi Mehra on Edstem
def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return -1

# From Avi Mehra on Edstem
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


n: int = 0
i: int = 0
j: int = 0

n = str_to_int(input())

while i < n:
    j = j + (i * i * i)
    i = i + 1

print(j)

