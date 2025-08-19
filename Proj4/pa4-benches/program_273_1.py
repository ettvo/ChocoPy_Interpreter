# Runs large number of list concats and index expressions
s:str = ""
i:int = 0
j:int = 0
result:[str] = None

s = input()
result = []
while i < len(s):
    j = 0
    while j < len(s):
        result = result + [s[i]] + [s[j]]
        j = j + 1
    i = i + 1

i = 0
while i < len(s):
    print(result[i])
    i = i+1
