import random

#While loop
number = random.randint(1,10)
print(number)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You Guessed {} ".format(guess))
        isGuessRight = True
    else :
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
    
#for loop
for x in range(0,11) :
    print(x)
    
