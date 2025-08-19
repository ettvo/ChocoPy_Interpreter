
def count_ns(s:str) -> int:
    r:int = 0
    i:int = 0
    temp:int = 0

    while i < len(s):
        temp = 8 * 8 * 8 * 8 * 8 + 1 # test constant sub 
        if s[i] == "n":
            r = r + 1
        i = i + 1
    return r

print(count_ns(input()))