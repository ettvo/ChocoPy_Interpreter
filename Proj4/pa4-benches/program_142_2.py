input_str: str = ""
l: int = 0
r: int = 0
move_left: bool = True

input_str = input()
r = len(input_str) - 1

while l <= r:
    if move_left:
        print(input_str[l])
        l = l + 1
    else:
        print(input_str[r])
        r = r - 1
    move_left = not move_left