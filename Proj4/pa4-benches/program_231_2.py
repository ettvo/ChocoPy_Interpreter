array: [int] = None
array2: [int] = None
inp : str = ""
j:int = 0
i:int = 0
array = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5, 6]
inp = input()
j = len(inp) - 1

while i < len(inp):
    while j >= 0:
        array = array + array2
        j = j - 1
    i = i + 1

print(len(array))