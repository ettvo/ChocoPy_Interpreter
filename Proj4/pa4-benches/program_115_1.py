s: str = "1"
i:int = 0
j:int = 1

s = input()
while i < len(s):
    j = 2 * j
    i = i + 1

print(j)
