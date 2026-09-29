import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "developer", "coding", "software", "program"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("=================================")
    print("      WELCOME TO HANGMAN!        ")
    print("=================================")
    print(f"Guess the word letter by letter. You have {max_attempts} wrong attempts allowed.\n")

    while incorrect_guesses < max_attempts:
        # Display current word progress
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Current word: " + " ".join(display_word))
        print(f"Incorrect attempts remaining: {max_attempts - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly:", secret_word)
            break

        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid alphabet.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")

    else:
        print("=================================")
        print(f"Game Over! You ran out of attempts.")
        print(f"The correct word was: {secret_word}")
        print("=================================")

if __name__ == "__main__":
    play_hangman()
