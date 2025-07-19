import random

# Predefined list of 5 words
word_list = ["apple", "tiger", "plane", "chair", "snake"]

# Randomly choose a word
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a display version of the word with underscores
display_word = ["_" for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", max_attempts, "incorrect guesses allowed.")
print("Word: ", " ".join(display_word))

while incorrect_guesses < max_attempts and "_" in display_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess! Attempts left:", max_attempts - incorrect_guesses)

    print("Word: ", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("-" * 30)

# Final outcome
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
