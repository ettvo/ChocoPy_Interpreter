s: str = ""
vowels: str = "aeiouAEIOU"
consonants: str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_num_vowels(x:str) -> int:
    count: int = 0
    elem: str = ""
    vowel: str = ""
    i: int = 0
    j : int = 0

    while i < len(x):
        j = 0
        elem = x[i]
        i = i + 1
        while j < len(vowels):
            vowel = vowels[j]
            j = j + 1
            if elem == vowel:
                count = count + 1
    return count

def count_num_consonants(x:str) -> int:
    count: int = 0
    elem: str = ""
    const: str = ""
    i: int = 0
    j : int = 0

    while i < len(x):
        j = 0
        elem = x[i]
        i = i + 1
        while j < len(consonants):
            const = consonants[j]
            j = j + 1
            if elem == const:
                count = count + 1
    return count

s = input()
while len(s) > 0:
    print(count_num_vowels(s))
    print(count_num_consonants(s))
    print(s)
    s = input()

print("done")