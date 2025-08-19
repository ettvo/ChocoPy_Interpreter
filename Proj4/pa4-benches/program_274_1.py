# multi-assign and many operands in binary expressions

s:str = ""
lst1:[str] = None
lst2:[str] = None
lst3:[object] = None
lst4:[object] = None

i:int = 0

lst1 = []

lst3 = [None]
lst4 = [None]
s = input()
while i < len(s) - 1:
    lst1 = lst2 = lst3[0] = lst4[0] = lst1 + [s[i]] + [s[i]] + [s[i]] + [s[i]] + [s[i]]
    i = i + 1

print(len(lst3[0]))
i = 0
while i < len(s) - 1:
    print(lst2[i])
    i = i + 1