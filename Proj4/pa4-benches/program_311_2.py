n: int = 0


def f(x: int, y: int):
    while x > 0:
        if x % 1000 == 0:
            print(x)
            return
        x = x - y

n = 100 * len(input())
f(n, 1)
