s: str = ""
i:int = 0
h:int = 0
s = input()
h = len(s) - 1
while i <= h-1:
    if (i % 2) == 0:
        print(s[i])
    i = i + 1


