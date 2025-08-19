# word guesser
secret:str = "hello world\n"
guess:str = ""

print("Guess the secret word:")
guess = input()

while(guess != secret):
    print("Incorrect, guess again.")
    guess = input()

print("You guessed it!")