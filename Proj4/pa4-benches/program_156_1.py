def num_a_in_string(string: str) -> int:
    char:str = ""
    i:int = 0
    count:int = 0

    while i < len(string):
        char = string[i]
        if char == "a":
            count = count + 1
        i = i + 1

    return count


s:str = ""
i:int = 0

s = input()
i = num_a_in_string(s)

print(i)



