from random import choice
import os
import time
from datetime import datetime

# File to store high score
HIGH_SCORE_FILE = 'high_score.txt'

def read_high_score():
    """Read the high score from a file."""
    try:
        with open(HIGH_SCORE_FILE, 'r') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return float('inf')  # Return infinity if file doesn't exist or invalid

def write_high_score(score):
    """Write the high score to a file."""
    with open(HIGH_SCORE_FILE, 'w') as file:
        file.write(str(score))

def main():
    # Define the range of numbers to guess from
    num_range = range(1, 11)
    
    # Function to clear the console
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Welcome message and game instructions
    time.sleep(1)
    print("***Welcome to the Number Guessing Game!***\n")
    time.sleep(2)
    print(f"I am thinking of a number between {num_range[0]} and {num_range[-1]}")
    time.sleep(2)
    print("You have a limited number of chances to guess this number correctly.\nGood luck!")
    time.sleep(6)

    clear_console()

    # Difficulty levels and corresponding chances
    difficulties = {1: ('Easy', 10), 2: ('Medium', 5), 3: ('Hard', 3)}
    chances = 0
    high_score = read_high_score()  # Load high score from file

    # Select difficulty level
    while True:
        print("Please select the difficulty level: ")
        print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
        try:
            level = int(input("Please enter your choice: "))
            if level in difficulties:
                time.sleep(1)
                print(f"Great! You have selected the {difficulties[level][0]} difficulty level.\nLet's start the game!")
                chances = difficulties[level][1]  # Set chances based on level
                break
        except (KeyError, ValueError):
            print("Invalid input. Please try again.")

    while True:
        number = choice(num_range)  # Random number to guess
        attempts = 0  # Reset attempts for each game
        while chances > 0:
            try:
                start_time = datetime.now()  # Start timer for the guess
                guess = int(input("\nEnter your guess: "))
                attempts += 1
                chances -= 1
                
                if guess == number:
                    timedelta = datetime.now() - start_time
                    print(f"Congrats! You guessed the correct number in {attempts} attempts and {timedelta.seconds} seconds.")

                    # Update high score if the current attempt count is less
                    if attempts < high_score:
                        high_score = attempts
                        write_high_score(high_score)  # Save new high score to file
                        print(f"New High Score! You guessed the number in {high_score} attempts.")

                    break
                elif guess > number:
                    print(f"Incorrect! The number is less than {guess}.\n")
                else:
                    print(f"Incorrect! The number is greater than {guess}.\n")
                    
            except ValueError:
                print("Please enter a valid integer.")

        # Ask if the player wants to continue
        x = input("\nWould you like to continue (y/n)? ").strip().lower()
        if x == 'n':
            print("\nThanks for playing! See you next time.")
            break
        elif x == 'y':
            chances = difficulties[level][1]  # Reset chances for the next round
            continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
