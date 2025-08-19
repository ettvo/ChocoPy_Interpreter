def a_in_string(string: str) -> bool:
    char:str = ""
    found_a:bool = False
    i:int = 0

    while i < len(string):
        char = string[i]
        if char == "a":
            found_a = True
        i = i + 1

    return found_a


s:str = ""
b:bool = False
s = input()
b = a_in_string(s)

if b:
    print(s)
else:
    print("does not contain a")


