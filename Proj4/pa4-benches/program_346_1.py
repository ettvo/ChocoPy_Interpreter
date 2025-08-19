s: str = ""
i: int = 0
l: [str] = None
l = []
s = input()
while i < len(s):
    l = l + [s[i], "abc"]

    i = i + 1
i = 0
while i < len(l):
    print(l[i])
    i = i + 1
