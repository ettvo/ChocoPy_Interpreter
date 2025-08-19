def split_print(s: str, split: str):
    i:int = 0 
    while i < len(s):
        if s[i] == split:
            print("--SPLIT--")
        else:
            print(s[i])
        i = i + 1

split_print(input(), "-")