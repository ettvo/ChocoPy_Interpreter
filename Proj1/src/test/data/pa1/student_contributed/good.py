lst = [1, 2, 3, 4, 5]

a = 3
b = True
c = False
d = 1 and 0
e = 20 or 6
f = 1 - 6
g = None
h = "hahahahahha"
i = not False
j = -1

def count(c:int, f:bool, n:str):
    i = c

    if i < 0:
        print("can't do negatives!")
        return
    
    while i < f:
        print(n[i])
        if i == 3:
            print("Here's a number " + n[i])
        i = i + 1

    count = 0
    for count in n:
        count = count + 1

    print("This is number " + count)

    return 0
        

x = 2
y = 4
count(x, y, lst)


    
    