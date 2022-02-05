import random

def guessing_game():
    number = random.randint(0,100)
    
    while True:
        guess = int(input("Guess the number to see if it is right: "))

        if guess == number:
            print(f"You've guessed the right number, yes it is indeed {guess}")
            return
        elif guess < number:
            print(f'The guess is too low, try again \n')
        else:
            print(f'The guessed number is too high! try again \n')

guessing_game()