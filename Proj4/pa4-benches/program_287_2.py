x:int = 0
the:str = ""

def str_get(s:str, i:int) -> str:
    return s[i]

the = input()
while x < len(the):
    print(str_get(the, len(the) - 1 - x))
    x = x + 1
