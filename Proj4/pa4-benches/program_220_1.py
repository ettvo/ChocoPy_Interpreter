def sum_of_a(n: str) -> int:
    # Function to calculate the sum of digits of a number
    sum: int = 0
    x: int = 0
 
    
    
    while x < len(n):
        if n[x] == "a":
            sum = sum + 1
        x = x + 1
    return sum

n:str = ""
n = input()
print(sum_of_a(n))
