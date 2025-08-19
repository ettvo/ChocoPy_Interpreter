#program to find element in list using binary search, assume element is in list

#first number is target
#rest are the numbers in the list, this must be sorted in order

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
        i = i + 1

    # Compute result
    return result * sign

s:str = ""
_list:[int] = None
i: int = 0
a: int = 0
append_list: [int] = None
first_char: bool = True
second_char: bool = True
target:int = 0
li:int = 0
done:bool = False
ri:int = 0
mi:int = 0

_list = []
s = input()
while len(s) > 0:
    if first_char:
        first_char = False
        target = str_to_int(s)
    else:
        if second_char:
            a = str_to_int(s)
            _list = [a]
            second_char = False
        else:
            a = str_to_int(s)
            append_list = [a]
            _list = _list + append_list
    s = input()

#find target and print index through bin search

ri = len(_list) - 1
mi = (li + ri) // 2

while not done:
    mi = (li + ri) // 2
    if _list[mi] == target:
        done = True
    elif _list[mi] > target:
        ri = mi - 1
    else:
        li = mi + 1
print(mi)




