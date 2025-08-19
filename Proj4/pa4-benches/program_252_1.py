
def str_to_int(x: str) -> int:
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i:int = 0

    # Parse digits
    while i < len(x):
        char = x[i]
        i = i + 1
        if char == "-":
            if not first_char:
                return 0 # Error
            sign = -1
        elif char == "0":
            digit = 0
        elif char == "1":
            digit = 1
        elif char == "2":
            digit = 2
        elif char == "3":
            digit = 3
        elif char == "3":
            digit = 3
        elif char == "4":
            digit = 4
        elif char == "5":
            digit = 5
        elif char == "6":
            digit = 6
        elif char == "7":
            digit = 7
        elif char == "8":
            digit = 8
        elif char == "9":
            digit = 9
        elif char == "\n":
            return result * sign
        else:
            return 0 # On error
        first_char = False
        result = result * 10 + digit

    # Compute result
    return result * sign

b:[str] = None
DO_SHT:int = 0
c:str = "baaa"
N:int = 0
i:int = 0

def call(c:str):
  j:int = 0
  def call2(c:str) -> int:
    j:int = 3
    while j < 30:
      j = j + 1
    return j
  
  print("HI")
  while j < 10:
    call2(c)
    j = j +1

head:[[[[[int]]]]] = None

N = str_to_int(input())
DO_SHT = str_to_int(input())

b = ["hgewagsdagew"]

while i < N:
  call(c)
  i = i + 1
i = 0
while i < DO_SHT:
  b = b + b
  i = i + 1
