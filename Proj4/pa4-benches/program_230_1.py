array: [int] = None
array2: [int] = None
inp : str = ""
i:int = 0
array = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5, 6]
inp = input()

while i < len(inp):
    array = array + array2
    i = i + 1

print(len(array))