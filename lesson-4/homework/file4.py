import random


def number_guessing_game():
    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 10

        print("Guess the number between 1 and 100. You have 10 attempts.")

        while attempts > 0:
            guess = int(input("Enter your guess: "))

            if guess > number_to_guess:
                print("Too high!")
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("You guessed it right!")
                break

            attempts -= 1
            print(f"You have {attempts} attempts left.")

        if attempts == 0:
            print("You lost. Want to play again?")

        play_again = input("Type 'Y', 'YES', 'y', 'yes', 'ok' to play again: ")
        if play_again not in ["Y", "YES", "y", "yes", "ok"]:
            break


number_guessing_game()
