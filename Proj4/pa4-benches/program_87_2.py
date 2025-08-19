a:str = ""
l:[str] = None
l = ["a"]
a = input()
while len(a) > 0 and len(l) < len(a):
    l = l + [a[0]]
print(l[len(l) - 1])