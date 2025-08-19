
input_string : str = ""
digit_string : str = ""
input_length : int = 0
digit : int = 0
index : int = 0
result : int = 0

input_string = input()
input_length = len(input_string)-1
	
# Benchmark test to sum digits
index = 0
result = 0
while index < input_length:
	digit_string = input_string[index]
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
	result = result + digit
	index = index + 1

print(result)
