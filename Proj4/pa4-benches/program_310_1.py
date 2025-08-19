
def side_fx(x: str) -> str:
    z:int = 0
    while z < len(x):
        z = z + 1
    print(z)
    return x

def no_fx(x:str):
    z:int = 0
    while z < len(x) * 5:
        z = z + 1

inp:str = ""

inp = input()

no_fx(inp)
side_fx(inp)