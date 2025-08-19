s: str = ""
char : str = ""
storage : str = ""
write_bool :bool = False


s = input()
while len(s) > 0:
    if (write_bool):
        storage = s
        write_bool = False
    elif (s == "read\n"):
        print(storage)
    elif (s == "write\n"):
        write_bool = True
    else:
        print("Not a command")
    s = input()