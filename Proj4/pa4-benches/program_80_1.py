def helper(k: int) -> int:
    return k - 3
def even_more_complicated(r: int) -> int:
    if r < 1:
        r = 1
    while r < 10:
        even_more_complicated(r+1)
        print(helper(r))
        r = r + 1
        print(r)
    return r - 4

length:int = 0
length = len(input())
length = length * 2
while length > 0:
    length = length - 10
    even_more_complicated(length)