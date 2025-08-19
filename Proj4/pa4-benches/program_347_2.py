s: str = ""
i: int = 0
next: int = 1
total: int = 0
total = -1
s = input()
while i < len(s):
    if i + 1 == next:
        total = total + 1
        next = next * 2
    i = i + 1

print(total)
