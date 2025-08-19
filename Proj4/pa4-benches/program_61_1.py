n1:int = 0
n2:int = 0

def euclidean_algorithm(n1:int, n2:int) -> int:
    if n1 > n2:
        return euclidean_algorithm(n2, n1)
    if n2 <= 0:
        return -1
    if n1 == 0:
        return n2
    return euclidean_algorithm(n2 % n1, n1)

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
        

n1 = str_to_int(input())
n2 = str_to_int(input()) 
print(euclidean_algorithm(n1, n2))

