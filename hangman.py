import random

WORDS = ["python", "developer", "computer", "internship", "programming"]
MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()

    print("\n=== CodeAlpha Hangman Game ===")
    print(f"The word has {len(word)} letters. You can make {MAX_WRONG_GUESSES} incorrect guesses.")

    while len(wrong_guesses) < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(word, guessed_letters))
        print("Incorrect guesses:", ", ".join(sorted(wrong_guesses)) or "None")
        print(f"Guesses remaining: {MAX_WRONG_GUESSES - len(wrong_guesses)}")

        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. Try another.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses.add(guess)
            print("Sorry, that letter is not in the word.")

    print(f"\nGame over! The word was: {word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in {"yes", "y"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
