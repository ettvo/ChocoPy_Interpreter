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

def is_prime(num: int) -> bool:
    i: int = 2
    if num <= 1:
        return False
    elif num <= 3:
        return True
    
    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 1
    return True

def nth_prime(N: int) -> int:
    num: int = 2
    while N > 0:
        if is_prime(num):
            N = N - 1
            if N == 0:
                return num
        num = num + 1
    return -1

print(nth_prime(str_to_int(input())))
