def str_to_int(string: str) -> int:
    # Takes in a string, which may end with a space or newline, and returns the integer value of the string
    # Integer must be between -2147483647 and 2147483647, inclusive
    # Usage: str_to_int("123")
    #        >>> 123
    # Usage: str_to_int("123\n    ")
    #        >>> 123
    # Usage: str_to_int(input()) <- -123
    #        >>> -123
    # By: Alex Goldberg
    result:int = 0
    digit:int = 0
    char:str = ""
    sign:int = 1
    first_char:bool = True
    i:int = 0

    while i < len(string):
        char = string[i]
        if char == "-":
            if not first_char:
                print("Error: Negative sign not at beginning of string")
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
        elif char == " " or char == "\n" or char == "\t":
            return result * sign # Assume whitespace or newline is end of string, return result
        else:
            print("Error: Invalid character in string")
            return 0 # Error
        first_char = False
        i = i + 1
        result = result * 10 + digit

    return result * sign

def mod_exp(base: int, exp: int, modulus: int) -> int:
    result: int = 1
    base = base % modulus
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % modulus
        exp = exp // 2
        base = (base * base) % modulus
    return result

def compute_mod_inverse(a: int, m: int) -> int:
    m0: int = 0
    y: int = 0
    x: int = 1
    q: int = 0
    t: int = 0
    m0 = m

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x

def rsa_encrypt(m: int, e: int, n: int) -> int:
    return mod_exp(m, e, n)

def rsa_decrypt(c: int, d: int, n: int) -> int:
    return mod_exp(c, d, n)

p: int = 61
q: int = 53
n: int = 0
phi: int = 0
e: int = 17
d: int = 0
message: int = 0
cipher: int = 0
decrypted_message: int = 0

n = p * q
phi = (p - 1) * (q - 1)
d = compute_mod_inverse(e, phi)

message = str_to_int(input())
cipher = rsa_encrypt(message, e, n)
decrypted_message = rsa_decrypt(cipher, d, n)

print(message)
print(cipher)
print(decrypted_message)