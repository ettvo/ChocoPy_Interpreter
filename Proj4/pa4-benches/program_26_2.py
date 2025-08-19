# function implemented by github copilot
def select_sort(arr:[int]) -> [int]:
	i:int = 0
	j:int = 0
	min_index:int = 0
	temp:int = 0
	while i < len(arr):
		min_index = i
		j = i + 1
		while j < len(arr):
			if arr[j] < arr[min_index]:
				min_index = j
			j = j + 1
		temp = arr[i]
		arr[i] = arr[min_index]
		arr[min_index] = temp
		i = i + 1
	return arr

string:str = ""
unsorted:[int] = None
sorted:[int] = None
i:int = 0
num:int = 0
digit:int = 0

def digit_to_int(digit:str) -> int:
	if string[i] == "0":
		return 0
	elif string[i] == "1":
		return 1
	elif string[i] == "2":
		return 2
	elif string[i] == "3":
		return 3
	elif string[i] == "4":
		return 4
	elif string[i] == "5":
		return 5
	elif string[i] == "6":
		return 6
	elif string[i] == "7":
		return 7
	elif string[i] == "8":
		return 8
	elif string[i] == "9":
		return 9
	else:
		return -1

unsorted = []
sorted = []

string = input()
while i < len(string):
	digit = digit_to_int(string[i])
	if digit >= 0:
		unsorted = unsorted + [digit]
	i = i + 1
sorted = select_sort(unsorted)
i = 0
while i < len(sorted):
	print(sorted[i])
	i = i + 1
