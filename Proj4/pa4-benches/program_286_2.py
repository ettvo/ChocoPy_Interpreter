def rev(s: str, index: int):
    while index >= 0:
        print(s[index])
        index = index - 1

input_str:str = ""
input_str = input()
rev(input_str, len(input_str) - 1)
