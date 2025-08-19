started:bool = False
startCheck:bool = False
startInt:bool = False
guessInt:bool = False

saveInt:int = 0
questions:int = 0

greaterCheck:bool = False
lessCheck:bool = False
divCheck:bool = False
retreivedInt:bool = False

def str_to_int(int_string:str)->int:
    char:str = ""
    i:int = 0
    tens:int = 1
    numbers:int = 0
    while i < len(int_string):
        char = int_string[len(int_string)-1-i]
        if (char == "0"):
            tens = tens * 10
        elif (char == "1"):
            numbers = numbers + tens
            tens = tens * 10
        elif (char == "2"):
            numbers = numbers + 2*tens
            tens = tens * 10
        elif (char == "3"):
            numbers = numbers + 3*tens
            tens = tens * 10
        elif (char == "4"):
            numbers = numbers + 4*tens
            tens = tens * 10
        elif (char == "5"):
            numbers = numbers + 5*tens
            tens = tens * 10
        elif (char == "6"):
            numbers = numbers + 6*tens
            tens = tens * 10
        elif (char == "7"):
            numbers = numbers + 7*tens
            tens = tens * 10
        elif (char == "8"):
            numbers = numbers + 8*tens
            tens = tens * 10
        elif (char == "9"):
            numbers = numbers + 9*tens
            tens = tens * 10
        elif (char == "\n"):
            pass
        else:
            print("this is not a positive number you entered, please try again")
            return -1
        i = i + 1
    return numbers
    
def guess_int(int_string: str)->bool:
    guessed: int = 0

    guessed = str_to_int(int_string)
    if(guessed == -1):
        return True
    if(guessed == saveInt):
        print("You have guessed it right! The number of questions used are:")
        print(questions)
        print("You can now start a new game.")
        return True
    else:
        print("You have guessed it wrong.")
        return False

def div_check(int_string: str)->bool:
    div: int = 0
    mod: int = 0

    div = str_to_int(int_string)
    if(div == -1):
        return True
    mod = saveInt % div
    if(mod == 0):
        print("The number is divisible by")
        print(div)
    else:
        print("The number is not divisible by")
        print(div)
    return False

def greater_check(int_string: str)->bool:
    greater: int = 0

    greater = str_to_int(int_string)
    if(greater == -1):
        return True
    if(greater > saveInt):
        print("This number is greater")
        print(greater)
    else:
        print("This number is not greater")
        print(greater)
    return False

def less_check(int_string: str)->bool:
    less: int = 0

    less = str_to_int(int_string)
    if(less == -1):
        return True
    if(less < saveInt):
        print("This number is lesser")
        print(less)
    else:
        print("This number is not lesser")
        print(less)
    return False

s: str = ""



s = input()
while len(s) > 0:
    if (started == False and s != "Start\n"):
        print("Game not started yet. Type Start to initialize")
    elif(started == False and s == "Start\n"):
        #initialize
        print("Player 1, please enter a positive int value.")
        started = True
        startCheck = False
        guessInt = False

        saveInt = 0
        questions = 0

        greaterCheck = False
        lessCheck = False
        divCheck = False
        retreivedInt = False
        startInt = True
    elif(startCheck):
        if(s == "Y\n"):
            print("Player 1, please enter a positive int value.")
            started = True
            startCheck = False
            guessInt = False

            saveInt = 0
            questions = 0

            greaterCheck = False
            lessCheck = False
            divCheck = False
            retreivedInt = False
            startInt = True

        elif(s == "N\n"):
            print("Game status kept")
            startCheck = False
        else:
            print("Are you sure you want to end current game? Y/N")

    elif(startInt):
        
        saveInt = str_to_int(s)
        if(saveInt == -1):
            saveInt = 0
        else:
            print("int saved, now the second player can start guessing")
            startInt = False
    elif(guessInt):
        if(not guess_int(s)):
            questions = questions + 1
    elif(divCheck):
        divCheck = div_check(s)
        if(not divCheck):
            questions = questions + 1
    elif(greaterCheck):
        greaterCheck = greater_check(s)
        if(not greaterCheck):
            questions = questions + 1
    elif(lessCheck):
        lessCheck = less_check(s)
        if(not lessCheck):
            questions = questions + 1

    elif(s == "Start\n"):
        print("Are you sure you want to end current game? Y/N")
        startCheck = True
    elif(s == "Commands\n"):
        print("Valid commands are: Guess to guess an int, Greater to check Wheter the given number is greater, Less to check whether the given number is lesser, Div to check whether the secret number is divisible by the given.")
    elif(s == "Guess\n"):
        guessInt = True
        print("Please type a positive int value")
    elif(s == "Greater\n"):
        greaterCheck = True
        print("Please type a positive int value")
    elif(s == "Less\n"):
        lessCheck = True
        print("Please type a positive int value")
    elif(s == "Div\n"):
        divCheck = True
        print("Please type a positive int value")
    else:
        print("Not a valid command, please type Commands to check valid commands")
    s = input()