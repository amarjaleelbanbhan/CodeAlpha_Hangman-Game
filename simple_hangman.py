"""
Simple Hangman Game - Basic Version
This is a more traditional implementation for comparison
"""

import random

def simple_hangman():
    # Basic word list
    words = ["PYTHON", "CODING", "GAMES", "CHALLENGE", "HANGMAN"]
    
    # Select random word
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    print("🎮 Welcome to Simple Hangman!")
    print(f"Guess the {len(word)}-letter word!")
    
    while wrong_guesses < max_wrong:
        # Display current progress
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        
        print(f"\nWord: {display}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check if won
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed '{word}'!")
            return
        
        # Get guess
        guess = input("Enter a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry! '{guess}' is not in the word.")
            wrong_guesses += 1
    
    print(f"\n💀 Game Over! The word was '{word}'")

if __name__ == "__main__":
    simple_hangman()
