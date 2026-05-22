import random

print(" Welcome to the Hangman Game ")
print("You need to guess the complete word in 6 tries.")
print("Maximum word length is 7 characters.")
print()

# List of 100 words (all <= 7 characters)
words = [
    "apple", "banana", "orange", "grapes", "mango", "papaya", "peach",
    "cherry", "guava", "melon", "kiwi", "plum", "lemon", "berry",
    "carrot", "potato", "onion", "tomato", "pickle", "radish",
    "python", "java", "coding", "debug", "binary", "search", "sort",
    "stack", "queue", "graph", "tree", "array", "string", "random",
    "school", "college", "teacher", "student", "library", "campus",
    "animal", "tiger", "lion", "zebra", "monkey", "rabbit", "panda",
    "guitar", "piano", "violin", "drums", "flute", "singer", "dance",
    "mobile", "laptop", "camera", "screen", "charger", "speaker",
    "winter", "summer", "spring", "autumn", "rainy", "cloudy",
    "doctor", "engine", "farmer", "lawyer", "artist", "writer",
    "planet", "earth", "saturn", "venus", "rocket", "galaxy",
    "cricket", "tennis", "hockey", "soccer", "boxing", "runner",
    "silver", "gold", "copper", "diamond", "pearl", "crystal",
    "bridge", "castle", "forest", "island", "desert", "river",
    "butter", "coffee", "biscuit", "noodle", "burger", "pizza",
    "friend", "family"
]

# Select random word
word = random.choice(words)

print("The length of the word is:", len(word))
print()

# Create hidden word
hidden_word = ["_"] * len(word)

tries = 6
won = False
guessed_letters = []

while tries != 0 and won == False:

    print("Word:", " ".join(hidden_word))
    print("Remaining tries:", tries)
    print("Guessed letters:", guessed_letters)
    
    guess = input("Enter a letter or complete word: ").lower()

    # If user enters full word
    if guess == word:
        won = True
        break

    # If user enters single letter
    elif len(guess) == 1:

        if guess in guessed_letters:
            print("You already guessed this letter.")
            print()
            continue

        guessed_letters.append(guess)

        if guess in word:

            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess

            print("Correct Guess!")
            print()

            # Check if word completed
            if "_" not in hidden_word:
                won = True

        else:
            tries -= 1
            print("Wrong Guess!")
            print()

    else:
        tries -= 1
        print("Wrong Word Guess!")
        print()

# Final Result
if won:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over!")
    print("The correct word was:", word)
