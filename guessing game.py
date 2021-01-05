import random

number = random.randint(1,10)
guess = -1
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > number:
        print('Your guess was too high')
    elif guess < number:
        print("Your guess was too low")
    else:
        print("You got it!")
