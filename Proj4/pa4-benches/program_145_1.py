x:str = " "

print("The goal is to keep your string length less than 10")
while (len(x) - 1) < 10 :
    if (x != " "):
        print("You said (with some adjustments):")
        print(x)

    if (len(x) - 1) % 2 == 0:
        if (x != " "):
            print("Size is divisible by 2!")
        x = input()
    elif (len(x) - 1) % 3 == 0:
        if (x != " "):
            print("Size is divisible by 3")
        x = input()
    else:
        print("You failed...")
        x = "0123456789101112131415"