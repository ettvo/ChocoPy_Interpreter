
def str_to_int(x: str) -> int:
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i:int = 0

    # Parse digits
    while i < len(x):
        char = x[i]
        i = i + 1
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        elif char == "\n":
            return result * sign
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign
    
def calloc(n:int, m:int) -> [[int]]:
    lst:[[int]] = None
    i:int = 0
    lst = [None]
    while len(lst) < n:
        lst = lst + lst

    while i < n:
        lst[i] = [-1]
        while len(lst[i]) < m:
            lst[i] = lst[i] + lst[i]
        i = i + 1
    

    return lst

def dp(mem:[[int]], num_items:int, capacity:int, weights:[int], value:[int]) -> int:
    def rec_dp(idx:int, c:int) -> int:
        res1:int = 0
        res2:int = 0
        res1 = -1
        res2 = -1
        if (idx >= num_items or c < 0):
            return -1
        if mem[idx][c] != -1:
            return mem[idx][c]
        
        res1 = rec_dp(idx + 1, c - weights[idx])
        if res1 != -1:
            res1 = res1 + value[idx]
        res2 = rec_dp(idx + 1, c) + 0

        if (res1 == -1 and res2 == -1):
            if (c >= weights[idx]):
                return value[idx]

        if (res1 == -1):
            mem[idx][c] = res2
            return res2
        if (res2 == -1):
            mem[idx][c] = res1
            return res1
        if (res1 <= res2):
            mem[idx][c] = res2
            return res2
        
        mem[idx][c] = res1
        return res1
    
    return rec_dp(0, capacity)

#this has 8192 zeros
mem:[[int]] = None
NUM_ITEMS:int = 0
CAPACITY:int = 0
WEIGHTS:[int] = None
VALUE:[int] = None
i:int = 0
j:int = 0
NUM_ITEMS = str_to_int(input())
CAPACITY = str_to_int(input())
WEIGHTS = [0]
VALUE = [0]
i = 0
while i < NUM_ITEMS:
    if i >= len(WEIGHTS):
        WEIGHTS = WEIGHTS + WEIGHTS
    WEIGHTS[i] = str_to_int(input())
    i = i + 1
i = 0
while i < NUM_ITEMS:
    if i >= len(VALUE):
        VALUE = VALUE + VALUE
    VALUE[i] = str_to_int(input())
    i = i + 1

mem = calloc(NUM_ITEMS, CAPACITY)

print(dp(mem, NUM_ITEMS, CAPACITY, WEIGHTS, VALUE))
