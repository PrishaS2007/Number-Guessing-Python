import random

# Menu Select
def number_guessing():
    play_game = True 

    while play_game:
        print("Number Guessing Game")
        print("Please select your level of difficulty.")
        print("1. Easy (12 guesses)")
        print("2. Medium (8 guesses)")
        print("3. Hard (4 guesses)")
        difficulty = input("Enter your choice (1-3): ")

        if difficulty == '1':
            max_guesses = 12
        elif difficulty == '2':
            max_guesses = 8
        elif difficulty == '3':
            max_guesses = 4
        else:
            print("Invalid Choice. Please select an option 1-3.")
            return

        # Get range of numbers from user
        low = int(input("Enter a low number for the number range: "))
        high = int(input("Enter a high number for the number range: "))

        # Generate a random number based on user input
        secret_number = random.randint(low, high)

        num_guesses = 0
        guess = None

        # Guessing Loop
        while num_guesses < max_guesses:
            try:
                guess = int(input("Enter a guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            num_guesses += 1

            if guess < secret_number:
                print("Too low. Try Again.\n")
            elif guess > secret_number:
                print("Too high. Try Again.\n")
            else:
                print(f"\nCongratulations! You guessed the number {secret_number} in {num_guesses} guesses. ")
                break

        # Player runs out of guesses
        if num_guesses == max_guesses and guess != secret_number:
            print(f"\nSorry, you ran out of guesses. The number I was thinking of was {secret_number}.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            play_game = False 
        else:
            print("\nLet's play again!\n")

if __name__ == "__main__":
    number_guessing()