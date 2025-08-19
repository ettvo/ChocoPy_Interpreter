s:str = ""

def outer(x:str) -> int:
    y:int = 2
    def inner() -> int:
        sum:int = 0
        sum = y * 3 + 123125 // len(x)
        if sum % 2 == 0:
            return sum % len(x)
        else:
            return sum % len(x) * 100
    return inner()

s = input()
while len(s) > 0:
    print(outer(s))
    s = input()