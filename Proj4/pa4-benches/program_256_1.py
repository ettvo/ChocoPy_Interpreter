s: str = ""

s = input()

while len(s) > 0: 
    print(s)
    
    if (s == "exit"):
        s = ""
    s = input()