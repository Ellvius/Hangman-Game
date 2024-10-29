# HANGMAN GAME

# import modules
import random
from hangman_art import hangman_art
from words import word_list

#get a random word out of all the words
def get_word():
    word = random.choice(word_list)
    return word.lower()


#game logic
def hangman(word):
    #initialise variables
    win = False
    guessed_letters = []
    guessed_words = []
    display_letters = '_ '*len(word)
    tries = 6

    # starting prompts
    print("\n")
    print("="*20 + " HANGMAN GAME "+"="*20)
    

    # each levels
    while not win and tries > 0:
        # print hangman 
        print(hangman_art[tries])
        print("Word:",display_letters)
        guess = input("Guess a letter or a word: ").lower()

        # if letter is guessed
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("⚠️  Letter", guess,"already guessed")
            elif guess not in word:
                print("❌ Letter", guess, "is not in the word!")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("✅ Correct! The letter", guess, "is in the word!" )
                guessed_letters.append(guess)
                word_as_list = list(display_letters)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index*2] = guess
                display_letters = "".join(word_as_list)

                if "_" not in display_letters:
                    win = True

        # if the word is guessed
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("⚠️ Word", guess, "already guessed")
            elif guess != word:
                print("❌", guess, "is incorrect!")
                tries-=1
                guessed_words.append(guess)
            else:
                win = True
                display_letters = word
        
        # invalid guess
        else:
            print("⚠️ Not a valid guess!")
        if not win and tries > 0:
            print("_"*54)
    
    if win:
        print("\n","="*20,"🏆CONGRATS🏆","="*20,"\n")
        print(f"You guessed the word {word.upper()} correctly !".center(50))
        print("\n")
    else:
        print("\n","="*20,"❗GAME OVER❗","="*20)
        print(hangman_art[0])
        print("\n" + "You are dead!".center(50) + "\n" + f"The word was {word.upper()}".center(50) + "\n")

# game initialize
def main():
    word = get_word()
    hangman(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        hangman(word)

if __name__ == "__main__":
    main()