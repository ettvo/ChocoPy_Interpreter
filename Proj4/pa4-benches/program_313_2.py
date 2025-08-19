# Test of 'input' function.

s: str = ""
char : str = ""
result : int = 0
bin_result : int = 0
i: int = 0
twos: int = 1
tens: int = 1

s = input()
while len(s) > 0:
    while i < len(s):
        char = s[i]
        if (char == "0"):
            twos = twos*2
            tens = tens*10
        if (char == "1"):
            result = result + twos
            bin_result = bin_result + tens
            twos = twos*2
            tens = tens*10
        i = i + 1
    print("Decimal:")
    print(result)
    print("Binary:")
    print(bin_result)

    s = input()
    i = 0
    result = 0
    bin_result = 0
    twos = 1
    tens = 1
    