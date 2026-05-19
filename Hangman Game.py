import random

# List of 5 predefined words
words = ["apple", "mango", "table", "chair", "house"]

# Choose random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Wrong guesses counter
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

# Main game loop
while wrong_guesses < max_wrong:

    display_word = ""

    # Show guessed letters and blanks
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter one letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Already guessed check
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Correct or wrong check
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The word was:", word)