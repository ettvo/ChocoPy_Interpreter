
input_string : str = ""
digit_string : str = ""
input_length : int = 0
digit : int = 0
index : int = 0
result : int = 0
multiplier : int = 0

# recursive factorial func
def fact(x : int) -> int:
	if x == 0:
		return 1
	else:
		return x * fact(x-1)

input_string = input()
input_length = len(input_string)-1
	
# Benchmark test factorial recursive
index = 0
multiplier = 1
while index < input_length:
	digit_string = input_string[input_length-1-index]
	if digit_string == "0":
		digit = 0
	elif digit_string == "1":
		digit = 1
	elif digit_string == "2":
		digit = 2
	elif digit_string == "3":
		digit = 3
	elif digit_string == "4":
		digit = 4
	elif digit_string == "5":
		digit = 5
	elif digit_string == "6":
		digit = 6
	elif digit_string == "7":
		digit = 7
	elif digit_string == "8":
		digit = 8
	elif digit_string == "9":
		digit = 9
	result = result + digit*multiplier
	multiplier = multiplier * 10
	index = index + 1

result = fact(result)

print(result)
