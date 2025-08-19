def helper(k: int) -> int:
    return k - 3
def more_complicated(r: int) -> int:
    if r < 1:
        r = 1
    while r < 10:
        print(helper(r))
        r = r + 1
        print(r)
    return r - 4

length:int = 0
length = len(input())
length = length * 2
while length > 0:
    length = length - 10
    more_complicated(length)