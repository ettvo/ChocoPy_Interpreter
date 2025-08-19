
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
def init_call():
    i:int = 0
    lst:[[[[[[str]]]]]] = None
    a:[str] = None
    b:[str] = None
    c:[str] = None
    d:bool = True
    if (DO_SHT > 0):
        a = ["fffffdsgsagaw"]
        b = a + ["eagwagea"]
        c = a + ["gaewgsdags"]
        print(b[0])
        print(c[0])
        print(DO_SHT)
        print(N)
        get_outta_here(8)
        while i < 10:
            if not (head is None):
                head[0] = [[[[i]]]]
                print(head[0][0][0][0][0])
            lst = [[[[[a]]]]]
            b = a + a + a + a 
            c = a + a + a + a
            d = (b[0][0][0] == c[0][0][0])
            i = i + 1
        
        if not (head is None):
            head[0] = [[[[-1]]]]

    head[0] = [[[[0]]]]


def get_outta_here(num:int):
  if num >= 0:
    get_outta_here(num - 1)
    get_outta_here(num - 1)

b:str = "hello"
DO_SHT:int = 0
c:str = "baaa"
N:int = 0
i:int = 0

head:[[[[[int]]]]] = None

N = str_to_int(input())
DO_SHT = str_to_int(input())

head = []
head = [[[[[5]]]]]
head[0][0][0][0][0] = -1

while i < N:
    init_call()
    head= head +[[[[[i]]]]]
    i = i + 1

i = 0
while i < N:
    print(head[i][0][0][0][0])

    i = i + 1