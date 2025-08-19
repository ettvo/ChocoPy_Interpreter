s:str=""
def count_digits(n: str) -> int:
    count: int = 0
    #temp: str = n[count]
    while count < len(n):
        count = count + 1
    return count

s = input()
while len(s) > 0:
    print(count_digits(s))
    s = input()