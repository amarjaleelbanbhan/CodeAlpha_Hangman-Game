import random
import time
import sys

class HangmanGame:
    def __init__(self):
        # Themed word categories with hints
        self.word_categories = {
            "🌟 SPACE": {
                "words": ["GALAXY", "NEBULA", "QUASAR", "COSMOS", "ASTEROID"],
                "hints": ["A stellar collection", "Colorful space cloud", "Bright cosmic object", "The entire universe", "Rocky space object"]
            },
            "🐾 ANIMALS": {
                "words": ["ELEPHANT", "OCTOPUS", "PENGUIN", "GIRAFFE", "BUTTERFLY"],
                "hints": ["Largest land mammal", "Eight-armed sea creature", "Tuxedo bird", "Tallest animal", "Colorful flying insect"]
            },
            "🏛️ ANCIENT": {
                "words": ["PYRAMID", "SPHINX", "PHARAOH", "TEMPLE", "ORACLE"],
                "hints": ["Ancient tomb structure", "Riddle-asking creature", "Egyptian ruler", "Sacred building", "Divine messenger"]
            },
            "🔬 SCIENCE": {
                "words": ["MOLECULE", "QUANTUM", "NEUTRON", "PLASMA", "ENZYME"],
                "hints": ["Tiny chemical unit", "Physics particle theory", "Neutral atomic particle", "Fourth state of matter", "Biological catalyst"]
            },
            "🎨 MYSTERY": {
                "words": ["ENIGMA", "CIPHER", "PUZZLE", "RIDDLE", "SECRET"],
                "hints": ["Mysterious problem", "Coded message", "Brain teaser", "Question with trick", "Hidden information"]
            }
        }
        
        # ASCII art for hangman stages (reversed for dramatic effect)
        self.hangman_stages = [
            """
   ┌─────┐
   │     │
   │     
   │     
   │     
   │     
───┴─────
SAFE! 🎉
            """,
            """
   ┌─────┐
   │     │
   │     😟
   │     
   │     
   │     
───┴─────
Uh oh...
            """,
            """
   ┌─────┐
   │     │
   │     😰
   │     │
   │     
   │     
───┴─────
Getting risky!
            """,
            """
   ┌─────┐
   │     │
   │     😨
   │    ╱│
   │     
   │     
───┴─────
One arm down!
            """,
            """
   ┌─────┐
   │     │
   │     😱
   │    ╱│╲
   │     
   │     
───┴─────
Both arms!
            """,
            """
   ┌─────┐
   │     │
   │     💀
   │    ╱│╲
   │    ╱
   │     
───┴─────
One leg left!
            """,
            """
   ┌─────┐
   │     │
   │     💀
   │    ╱│╲
   │    ╱ ╲
   │     
───┴─────
GAME OVER! 💀
            """
        ]
        
        self.reset_game()
    
    def reset_game(self):
        """Reset game state for a new round"""
        self.max_wrong_guesses = 6
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.current_word = ""
        self.current_hint = ""
        self.current_category = ""
        self.game_over = False
        self.won = False
        
    def display_title(self):
        """Display animated title screen"""
        title = """
╔══════════════════════════════════════════════════╗
║                                                  ║
║    🎯 ULTIMATE HANGMAN CHALLENGE 🎯            ║
║                                                  ║
║        ┌─────┐     Welcome to the most          ║
║        │     │     unique Hangman experience!   ║
║        │     😊                                  ║
║        │    ╱│╲    • Themed Categories           ║
║        │    ╱ ╲    • Dynamic Hints              ║
║        │           • ASCII Animations           ║
║    ────┴─────      • Special Power-ups          ║
║                                                  ║
╚══════════════════════════════════════════════════╝
        """
        
        print("\033[1;36m" + title + "\033[0m")  # Cyan color
        time.sleep(1)
    
    def choose_category_and_word(self):
        """Let player choose category or use random selection"""
        print("\n🎲 Choose your destiny:")
        print("1. 🎯 Choose a category")
        print("2. 🎰 Random surprise!")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            print("\n📚 Available Categories:")
            categories = list(self.word_categories.keys())
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            
            try:
                cat_choice = int(input(f"\nChoose category (1-{len(categories)}): ")) - 1
                if 0 <= cat_choice < len(categories):
                    selected_category = categories[cat_choice]
                else:
                    selected_category = random.choice(categories)
                    print(f"Invalid choice! Randomly selected: {selected_category}")
            except ValueError:
                selected_category = random.choice(categories)
                print(f"Invalid input! Randomly selected: {selected_category}")
        else:
            selected_category = random.choice(list(self.word_categories.keys()))
            print(f"\n🎲 Random category selected: {selected_category}")
        
        # Select word and hint from chosen category
        category_data = self.word_categories[selected_category]
        word_index = random.randint(0, len(category_data["words"]) - 1)
        
        self.current_word = category_data["words"][word_index]
        self.current_hint = category_data["hints"][word_index]
        self.current_category = selected_category
        
        time.sleep(1)
    
    def display_game_state(self):
        """Display current game state with fancy formatting"""
        # Clear screen effect
        print("\n" * 2)
        print("═" * 60)
        print(f"🎮 CATEGORY: {self.current_category}")
        print(f"💡 HINT: {self.current_hint}")
        print("═" * 60)
        
        # Display hangman
        print(self.hangman_stages[self.wrong_guesses])
        
        # Display word progress with fancy formatting
        word_display = ""
        for letter in self.current_word:
            if letter in self.guessed_letters:
                word_display += f"🔤 {letter} "
            else:
                word_display += "❓ _ "
        
        print(f"🎯 WORD: {word_display}")
        print(f"💔 Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        
        # Display guessed letters with color coding
        if self.guessed_letters:
            correct_letters = [l for l in self.guessed_letters if l in self.current_word]
            wrong_letters = [l for l in self.guessed_letters if l not in self.current_word]
            
            if correct_letters:
                print(f"✅ Correct: {' '.join(sorted(correct_letters))}")
            if wrong_letters:
                print(f"❌ Wrong: {' '.join(sorted(wrong_letters))}")
        
        print("═" * 60)
    
    def get_player_guess(self):
        """Get and validate player's guess with special commands"""
        while True:
            print("\n🎯 Your options:")
            print("• Enter a letter to guess")
            print("• Type 'HINT' for an extra hint (1 use per game)")
            print("• Type 'WORD' to guess the entire word")
            
            guess = input("\n📝 Your guess: ").upper().strip()
            
            # Special commands
            if guess == "HINT":
                return self.use_hint()
            elif guess == "WORD":
                return self.guess_whole_word()
            elif len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print(f"⚠️  You already guessed '{guess}'! Try again.")
                    continue
                return guess
            else:
                print("⚠️  Please enter a single letter, 'HINT', or 'WORD'!")
    
    def use_hint(self):
        """Provide an additional hint (one-time use)"""
        if hasattr(self, 'hint_used'):
            print("❌ You already used your hint!")
            return self.get_player_guess()
        
        # Reveal a random unguessed letter
        unguessed_letters = [l for l in self.current_word if l not in self.guessed_letters]
        if unguessed_letters:
            hint_letter = random.choice(unguessed_letters)
            print(f"💡 BONUS HINT: The word contains the letter '{hint_letter}'!")
            self.hint_used = True
            return hint_letter
        else:
            print("🤔 All letters are already revealed!")
            return self.get_player_guess()
    
    def guess_whole_word(self):
        """Allow player to guess the entire word"""
        word_guess = input("🎯 Enter your word guess: ").upper().strip()
        if word_guess == self.current_word:
            print("🎉 INCREDIBLE! You guessed the whole word!")
            self.won = True
            self.game_over = True
            return None
        else:
            print(f"❌ '{word_guess}' is not correct!")
            self.wrong_guesses += 1
            return None
    
    def process_guess(self, guess):
        """Process the player's letter guess"""
        if guess is None:  # Whole word guess was processed
            return
        
        self.guessed_letters.add(guess)
        
        if guess in self.current_word:
            print(f"🎉 Great job! '{guess}' is in the word!")
            
            # Check if word is complete
            if all(letter in self.guessed_letters for letter in self.current_word):
                self.won = True
                self.game_over = True
        else:
            print(f"💔 Sorry! '{guess}' is not in the word.")
            self.wrong_guesses += 1
            
            # Check if game is lost
            if self.wrong_guesses >= self.max_wrong_guesses:
                self.game_over = True
    
    def display_end_game(self):
        """Display end game message with celebration or commiseration"""
        print("\n" + "🎊" * 60)
        
        if self.won:
            victory_msg = f"""
🏆 CONGRATULATIONS! YOU WON! 🏆

✨ You successfully guessed: {self.current_word}
🎯 Category: {self.current_category}
💔 Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}
⭐ You're a word wizard! ⭐
            """
            print("\033[1;32m" + victory_msg + "\033[0m")  # Green color
        else:
            defeat_msg = f"""
💀 GAME OVER! 💀

😢 The word was: {self.current_word}
🎯 Category: {self.current_category}
💡 Hint was: {self.current_hint}
🎮 Better luck next time, word warrior!
            """
            print("\033[1;31m" + defeat_msg + "\033[0m")  # Red color
        
        print("🎊" * 60)
    
    def play_again(self):
        """Ask if player wants to play another round"""
        while True:
            choice = input("\n🎮 Want to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("⚠️  Please enter 'y' for yes or 'n' for no!")
    
    def run_game(self):
        """Main game loop"""
        self.display_title()
        
        while True:
            self.reset_game()
            self.choose_category_and_word()
            
            print(f"\n🚀 Let's start! You're guessing a {len(self.current_word)}-letter word.")
            time.sleep(1)
            
            # Main guessing loop
            while not self.game_over:
                self.display_game_state()
                guess = self.get_player_guess()
                self.process_guess(guess)
                
                if not self.game_over:
                    time.sleep(1)  # Brief pause for dramatic effect
            
            # End game
            self.display_game_state()
            self.display_end_game()
            
            if not self.play_again():
                break
        
        print("\n🎮 Thanks for playing Ultimate Hangman Challenge!")
        print("💫 See you next time, word master! 💫")

# Run the game
if __name__ == "__main__":
    try:
        game = HangmanGame()
        game.run_game()
    except KeyboardInterrupt:
        print("\n\n🎮 Game interrupted! Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("🔧 Please try running the game again!")
