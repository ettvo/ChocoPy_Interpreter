def totient(x:int) -> int:
    def euclidean_algorithm(n1:int, n2:int) -> int:
        if n1 == 0:
            return n2
        return euclidean_algorithm(n2 % n1, n1)

    i:int = 0
    count:int = 0
    while i <= x:
        if euclidean_algorithm(i, x) == 1:
            count = count + 1
        i = i + 1
    return count

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

n:int = 0
i:int = 1

n = str_to_int(input())
while i < n:
    print(totient(i))
    i = i + 1


