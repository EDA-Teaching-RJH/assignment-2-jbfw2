### Part Two -- your code goes here. 
import random
number = random.randint(1,100)
guess = None
while guess != number:
    guess = int(input("Guess a number between 1 and 100!"))
    if guess < number:
        print("Too low. guess again")
    elif guess > number:
        print("Too high. Guess again")    
    else:
        print(f"Well done. {number} is the correct answer")