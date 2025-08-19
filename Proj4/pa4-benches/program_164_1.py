# these two functions below are by Avi Mehra from edstem under pre pa4 assignment
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
def fib(n:int) -> int :
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
x:int = 0
print("fib numbers! ")
x = str_to_int(input()) 

print("fib input:")
print(x)
print("fib output:")
print(fib(x))