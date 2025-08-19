s:str=""
def reverse_number(n: str) -> int:
    result: [str] = None
    i: int = 0  # Start from the last character of the string
    result = []  # Initialize an empty result string
    
    i = len(s) - 1
    while i >= 0:
        result = result + [n[i]]
        i = i - 1
    
    return len(result)

s = input()
while len(s) > 0:
    print(reverse_number(s))
    s = input()