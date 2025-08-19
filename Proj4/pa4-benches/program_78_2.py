def to_complicate(r: int) -> int:
    if r > 5:
        to_complicate(r-1)
        to_complicate(r-2)
        to_complicate(r-3)
    return r - 4
length:int = 5
length = len(input())
while length > 0:
    print(to_complicate(length))
    length = length - 1