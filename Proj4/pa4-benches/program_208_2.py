# Compute x**y
s: str = ""
def exp(x: int, y: int) -> int:
	a: int = 0
	def f(i: int) -> int:
		nonlocal a
		def geta() -> int:
			return a
		if i <= 0:
			return geta()
		else:
			a = a * x
			return f(i-1)
	a = 1
	return f(y)

# Input parameter
n:int = 42
# Run [0, n]
i:int = 0
s = input()
# Crunch
while len(s) > 0:
	print(3)
	print(s)
	print(exp(len(s),3))
	i = i + 1
	s = input()