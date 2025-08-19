s: str = ""

s = input()

while len(s) > 0: 
    print(s)
    s = input()
    while s == "continue":
        print(s)
        s = input()