def monkey_alphabet(i:int, seed:int):
    alph:str = ""
    c_num:int = 0
    char:str = ""

    # Lots of spaces at end so words aren't too long
    alph = "abcdefghijklmnopqrstuvwxyz"

    while i > 0:
        # Come up with a letter
        c_num = seed % len(alph)
        char = alph[c_num]

        # Append to our monkey novel
        print(char)

        # Monkey neurons firing
        seed = monkey(seed)

        i = i - 1

    return 

def monkey(seed:int) -> int:
    # Basic Example From: https://stackoverflow.com/questions/506118/how-to-manually-generate-random-numbers
    seed = seed * 1103515245 + 12345
    return (seed // 65536) % 32768
        


# Using another student's code snippet
# Ed: Instructor Shadaj Laddad Post: #272bf
#  "For this assignment, you are free to use snippets posted by other students, just add a comment saying so."
# ---------------
def char_to_int(char: str) -> int:
    i: int = 0

    while i < 10:
        if "0123456789"[i] == char:
            return i
        i = i + 1

    return -1

def str_to_int(string: str) -> int:
    result: int = 0
    i: int = 0

    while i < len(string):
        if char_to_int(string[i]) != -1:
            result = result * 10 + char_to_int(string[i])
        i = i + 1

    if string[0] == "-":
        return -result
    return result
# ---------------

str_input:str = ""
i:int = 0
seed:int = 0
out:str = ""

# Input parameter
str_input = input()
i = str_to_int(str_input)
str_input = input()
seed = str_to_int(str_input)

    
monkey_alphabet(i, seed)
