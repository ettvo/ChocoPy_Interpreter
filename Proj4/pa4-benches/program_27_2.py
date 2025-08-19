# remove all E's from a string
source:str = ""
i:int = 0

source = input()
while i < len(source):
	if source[i] != "E" and source[i] != "e":
		print(source[i])
	i = i + 1
