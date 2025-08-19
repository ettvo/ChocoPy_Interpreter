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


def goldbach_conjecture(n:int) -> [int]:
    i:int = 2
    def is_prime(n:int) -> bool:
        i:int = 2
        while i <= n // 2:
            if n % i == 0:
                return False
            i = i + 1
        return True

    if n % 2 != 0:
        return None
    while i < n:
        if is_prime(i) and is_prime(n - i):
            return [i, n - i]
        i = i + 1
    return None

n:int = 0
i:int = 4
lst:[int] = None

n = str_to_int(input())
n = 2 * n 
while i <= n:
    lst = goldbach_conjecture(i)
    if lst is None:
        print("help")
    else:
        print(lst[0])
        print(lst[1])
    print("")
    i = i + 2
    
