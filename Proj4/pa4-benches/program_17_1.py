def a_counter(val: str) -> int:
    # takes in a string and returns the number of a's that occur in the string
    counter: int = 0
    v: str = ""
    index: int = 0

    while index < len(val):
        v = val[index]
        if v == "a":
            counter = counter + 1
        index = index + 1
    return counter


print(a_counter(input()))
