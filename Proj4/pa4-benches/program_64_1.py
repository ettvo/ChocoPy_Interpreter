p:int = 0
private_key:int = 0

    
def evaluate_private_key(x:int) -> int:
    y:int = 2
    i:int = 1
    j:int = 1
    while (i * (263 - 1)) % (163 - 1) != 0:
        i = i + 1
    i = i * (263 - 1)
    
    while (j * x) % i != 1:
        if (j * x) % i == 0:
            return -1
        j = j + 1
    y = j
    return y

def str_to_int(s:str) -> int:
    i:int = 0
    j:int = 0
    num:int = 0
    while i < len(s):
        j = 0
        while j < 10:
            if "0741852963"[j] == s[i]:
                num = 10 * num + (j * 7) % 10
            j = j + 1
        i = i + 1

    return num

p = 163 * 263
private_key = evaluate_private_key(str_to_int(input()))
print(private_key)

