# Number Guessing Game
import random
print("Guess the number between 1 and 100")
print("You have only 5 attempts\n")
a = random.randint(1, 100)
tries = 5
while tries > 0:
    print("Enter a number:")
    num = int(input())
    if num == a:
        print("You guessed it right!")
        break
# It is essntial to check whether the diffrence between required and entered is greater than 50% or not
    diff = abs(a - num)
    if num < a:
        if diff >= a * 0.5:
            print("Required number is MUCH MORE")
        else:
            print("Required number is MORE")
    else:
        if diff >= a * 0.5:
            print("Required number is MUCH LESS")
        else:
            print("Required number is LESS")
    tries -= 1
    print("Remaining tries:", tries, "\n")
#As the total no of tries were completed you lost the game  
if tries == 0:
    print("You lost! The number was:", a)
