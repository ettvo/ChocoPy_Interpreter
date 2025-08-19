s:str = ""
x:int = 0
a:int = 0
s = input()
x = len(s)

while a < x:
    if a % 2 == 0:
        print(s[a])
    a = a + 1


