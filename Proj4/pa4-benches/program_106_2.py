word1:str = ""
word2:str = ""
word3:str = ""
word4:str = ""
rev1:[str] = None
rev2:[str] = None
rev3:[str] = None
rev4:[str] = None
lst_idx:int = 0
def reverse(s:str) -> [str]:
    reversed_lst:[str] = None
    idx:int = 0
    reversed_lst = []
    idx = len(s) - 1
    while idx >= 0:
        reversed_lst = reversed_lst + [s[idx]]
        idx = idx - 1
    idx = 0
    return reversed_lst

word1 = input()
word2 = input()
word3 = input()
word4 = input()

rev1 = reverse(word1)
rev2 = reverse(word2)
rev3 = reverse(word3)
rev4 = reverse(word4)

if len(rev1) > len(rev2) and len(rev1) > len(rev3) and len(rev1) > len(rev4):
    while lst_idx < len(rev1):
        print(rev1[lst_idx])
        lst_idx = lst_idx + 1
elif len(rev2) > len(rev2) and len(rev2) > len(rev2):
    while lst_idx < len(rev2):
        print(rev2[lst_idx])
        lst_idx = lst_idx + 1
elif len(rev3) > len(rev4):
    while lst_idx < len(rev3):
        print(rev3[lst_idx])
        lst_idx = lst_idx + 1
else:
    while lst_idx < len(rev4):
        print(rev4[lst_idx])
        lst_idx = lst_idx + 1
