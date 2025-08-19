a: str = ""
i: int = 0
found: bool = False
a = input()
while i < len(a) - 1:
    if found == False:
        if a[i] == "a":
            print(i)
            found = True
    i = i + 1