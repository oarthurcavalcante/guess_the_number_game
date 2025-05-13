import random
from art import logo

print(logo)

game_level = input(f'Welcome to the Number Guessing Game!\n'
      f'Here is how to play:\n'
      f'I am thinking on a number between 1 and 100\n'
      f'Choose a difficulty. Type \'easy\' or \'hard\':\n')

number_of_choices = {
    "easy": 10 ,
    "hard": 5}

number_to_be_guessed = random.randint( 1 , 100)

def guess_number():

    chances = number_of_choices[game_level]
    print(f"You have {chances} attempts to guess the number.")

    guess = int(input(f"Make a guess:"))

    while guess != number_to_be_guessed:
        chances -= 1
        if guess > number_to_be_guessed and chances > 0:
            print(f"\n"
                  f"Too high. \n" 
                  f"Guess again \n"
                  f"You have {chances} attempts to guess the number.")
            guess = int(input(f"Make a guess:"))
        elif guess < number_to_be_guessed and chances > 0:
            print(f"\n"
                  f"Too low. \n"
                  f"Guess again \n"
                  f"You have {chances} attempts to guess the number.")
            guess = int(input(f"Make a guess:"))
        elif guess == number_to_be_guessed and chances != 0:
            print("You won!")
            return
        elif chances == 0:
            print("\n"
                  "Chances over! \n"
                  "You lost!")
            return
        else:
            print("\n"
                  "Error")
            return


guess_number()


