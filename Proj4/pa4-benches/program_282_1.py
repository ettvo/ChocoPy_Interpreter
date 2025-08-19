# FIB MOD program

MOD: int = 10007
k: int = 0
ID: [[int]] = None
MAT: [[int]] = None
ret: [[int]] = None


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


def matmul(a: [[int]], b: [[int]]) -> [[int]]:
    ret: [[int]] = None
    ret = [[0, 0], [0, 0]]
    ret[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD
    ret[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD
    ret[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD
    ret[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD
    return ret


ret = [[1, 0], [0, 1]]
MAT = [[0, 1], [1, 1]]

k = str_to_int(input())

while k > 0:
    if k % 2 == 1:
        ret = matmul(ret, MAT)
    MAT = matmul(MAT, MAT)
    k = k // 2

print((ret[0][1] + ret[1][1]) % MOD)
