x:int = 0
the:str = ""
a:str = ""

def str_get(s:str, i:int) -> str:
    return s[i]

the = input()
while x < len(the):
    a = str_get(the, x)
    x = x + 1
    print(a)
