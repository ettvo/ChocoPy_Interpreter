
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

def sort(arr:[int]) -> [int]:
    temp_array:[int] = None
    
    def merge_sort(lo:int, hi:int):
        temp:int = 0
        mid:int = 0
        i1:int = 0
        i2:int = 0
        j:int = 0
        pick_first:bool = False
        mid = (lo + hi) // 2
        j = lo
        i1 = lo
        i2 = mid
        if lo == hi:
            return
        if lo + 1 == hi:
            return
        
        merge_sort(lo, mid)
        merge_sort(mid, hi)

        while j < hi:
            if (i1 < mid and i2 < hi):
                if (arr[i1] < arr[i2]):
                    pick_first = True
                else:
                    pick_first = False
            elif (i1 < mid):
                pick_first = True
            elif (i2 < hi):
                pick_first = False

            if pick_first:
                temp_array[j] = arr[i1]
                i1 = i1 + 1
            else:
                temp_array[j] = arr[i2]
                i2 = i2 + 1                 
            j = j + 1

        j = lo
        while j < hi:
            arr[j] = temp_array[j]
            j = j + 1
    
    temp_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while len(temp_array) < N:
        temp_array = temp_array + temp_array
    merge_sort(0, len(arr))
                
#this has 8192 zeros
in_array:[int] = None
N:int = 0
i:int = 0


N = str_to_int(input())
in_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while len(in_array) < N:
    in_array = in_array + in_array

while i < N:
    in_array[i] = str_to_int(input())
    i = i + 1
sort(in_array)

i = 0
while i < N:
    print(in_array[i])
    i = i + 1
