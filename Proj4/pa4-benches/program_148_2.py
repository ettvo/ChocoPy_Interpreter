x:str = ""
y:int = 0
z:int = 0
result:int = 0

def efficient_multiply(a:int, b:int) -> int:
    resulta:int = 0
    resultb:int = 0

    while (b > 0):
        resulta = resulta + a
        b = b - 1

    while (a > 0):
        resultb = resultb + b
        a = a - 1

    if (resulta == resultb):
        return resultb
    else:
        return resulta

def str_to_int(z:str) -> int:
    index:int = 0
    value:int = 0
    power:int = 1

    index = len(z) - 1
    while (index >= 0):
        if z[index] == "1":
            value = value + 1 * power
        if z[index] == "2":
            value = value + 2 * power
        if z[index] == "3":
            value = value + 3 * power
        if z[index] == "4":
            value = value + 4 * power
        if z[index] == "5":
            value = value + 5 * power
        if z[index] == "6":
            value = value + 6 * power
        if z[index] == "7":
            value = value + 7 * power
        if z[index] == "8":
            value = value + 8 * power
        if z[index] == "9":
            value = value + 9 * power
        index = index - 1
        power = power * 10
    return value

print("Enter a number to multiply:")
x = input()
y = str_to_int(x)
print("Enter another number to multiply:")
x = input()
z = str_to_int(x)
print("The number is now multiplied:")
print(efficient_multiply(y, z))
