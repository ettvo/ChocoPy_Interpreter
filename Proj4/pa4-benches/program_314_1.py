s: str = ""
char : str = ""
numbers : int = 0
i: int = 0
tens: int = 1


s = input()
while len(s) > 0:
    while i < len(s):
        char = s[i]
        if (char == "0"):
            tens = tens * 10
        elif (char == "1"):
            numbers = numbers + tens
            tens = tens * 10
        elif (char == "2"):
            numbers = numbers + 2*tens
            tens = tens * 10
        elif (char == "3"):
            numbers = numbers + 3*tens
            tens = tens * 10
        elif (char == "4"):
            numbers = numbers + 4*tens
            tens = tens * 10
        elif (char == "5"):
            numbers = numbers + 5*tens
            tens = tens * 10
        elif (char == "6"):
            numbers = numbers + 6*tens
            tens = tens * 10
        elif (char == "7"):
            numbers = numbers + 7*tens
            tens = tens * 10
        elif (char == "8"):
            numbers = numbers + 8*tens
            tens = tens * 10
        elif (char == "9"):
            numbers = numbers + 9*tens
            tens = tens * 10
        i = i + 1
    print(numbers)
    s = input()
    i = 0
    tens = 1