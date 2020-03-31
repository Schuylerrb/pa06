"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

def generate_random_word():
   import random
   wordslist_demo = "acres adult advice arrangement attempt August Autumn border breeze brick calm canal Casey cast claws coach constantly contrast cookies customs damage Danny deeply depth discussion doll donkey Egypt Ellen essential exchange exist explanation facing film finest fireplace floating folks fort garage grabbed grandmother habit happily Harry heading hunter Illinois image independent instant January kids label Lee lungs manufacturing Martin mathematics melted memory mill mission monkey Mount mysterious neighborhood Norway nuts occasionally official ourselves palace Pennsylvania Philadelphia plates poetry policeman positive possibly practical pride promised recall relationship remarkable require rhyme rocky rubbed rush sale satellites satisfied scared selection shake shaking shallow shout silly simplest slight slip slope soap solar species spin stiff swung tales thumb tobacco toy trap treated tune University vapor vessels wealth wolf zoo".split()
   word_demo = random.choice(wordslist_demo)
   return word_demo

def play_hangman():
    print("Welcome to hangman. Guess the mystery word and you win!")
    word = generate_random_word()
    word = word.lower()
    guessed_letters = []
    guesses_left = 10
    done = True
    mystery_word = list("-"*len(word))
    mystery_word1 = list(word)
    while done == True:
        print("------------------")
        if "-" not in mystery_word:
            print("You win! Great job.")
            print("You correctly guessed",word,end="")
            print("!")
            print("You can play again if you want.")
            print("------------------")
            break
        if guesses_left == 0:
            print("Sorry, you lose.")
            print("The word was...",word,end="")
            print("!")
            print("You can play again if you want.")
            print("------------------")
            break
        print("You have", guesses_left, "guesses left.")
        print(mystery_word)
        print("Guesses:",guessed_letters)
        letter_guess = input("Guess a letter.")
        letter_guess = letter_guess.lower()
        if len(letter_guess) != 1:
            print("Please guess 1 new letter.")
            continue
        elif letter_guess not in "qwertyuiopasdfghjklzxcvbnm":
            print("Please guess a letter.")
            continue
        elif letter_guess in guessed_letters:
            print("Please guess a new letter.")
            continue
        else:
            if letter_guess in word:
                print("Correct guess!")
                counter = -1
                for x in mystery_word1:
                    counter += 1
                    if x == letter_guess:
                        mystery_word[counter] = mystery_word1[counter]
                continue
            elif letter_guess not in word:
                print("Try again.")
                guesses_left = guesses_left - 1
                guessed_letters.append(letter_guess)
                continue
    while True:
        play_again = input("Would you like to play hangman again? Y/N")
        play_again = play_again.lower()
        if play_again == "y":
            play_hangman()
        elif play_again == "n":
            print("Goodbye!")
            break
        else:
            print("Please indicate if you would like to play hangman again.")
            continue



if __name__ == '__main__':
    play_hangman()
