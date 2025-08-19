alphabet: str = "$abcdefghijklmnopqrstuvwxyz"
s: str = ""
c: str = ""
i: int = 0
j: int = 0

s = input()
while i < len(s):
    c = s[i]
    j = 0
    while j < len(alphabet):
        if c == alphabet[j]:
            print(alphabet[j - 1])
            j = len(alphabet)
        j = j + 1
    i = i + 1
