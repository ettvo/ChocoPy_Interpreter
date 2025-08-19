def handle_vowel(string:str, i:int):
	def handle_consonant():
		nonlocal i

		while i < len(string) and not (string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
			print("consonant")
			i = i + 1
		handle_vowel(string, i)

	if i == len(string):
		return
	while i < len(string) and (string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
		print("vowel")
		i = i + 1
	handle_consonant()

handle_vowel(input(), 0)
