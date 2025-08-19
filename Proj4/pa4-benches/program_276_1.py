# Fibonacci with assign evaluation order

def str_to_int(s:str) -> int:
    result:int = 0
    i:int = 0
    
    while i < len(s) - 1:
        result = 10 * result
        if s[i] == "1":
            result = result + 1
        elif s[i] == "2":
            result = result + 2
        elif s[i] == "3":
            result = result + 3
        elif s[i] == "4":
            result = result + 4
        elif s[i] == "5":
            result = result + 5
        elif s[i] == "6":
            result = result + 6
        elif s[i] == "7":
            result = result + 7
        elif s[i] == "8":
            result = result + 8
        elif s[i] == "9":
            result = result + 9
        
        i = i + 1
    
    return result

def fib(n:int) -> int:
    result:int = 0
    if n == 0 or n == 1:
        return n
    result = fib(n - 1) + fib(n - 2)
    print(result)
    return result

i:int = 0
s:str = ""

s = input()
i = str_to_int(s)

fib(i)