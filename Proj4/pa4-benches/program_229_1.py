input_string: str = ""
count: int = 0
char_list: [str] = None
doubled_string: str = ""
i: int = 0
ch: str = ""

# Initialize variables
count = 0
i = 0

# Take input from the user
input_string = input()

# Count the number of non-space characters
while i < len(input_string):
    ch = input_string[i]
    if ch != " ":
        count = count + 1
    i = i + 1
print(count)  # Print the count of non-space characters
