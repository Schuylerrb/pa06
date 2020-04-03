"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

def generate_random_word():
   import random
   wordslist_demo = "acres adult advice arrangement attempt August Autumn border breeze brick calm canal Casey cast claws coach constantly contrast cookies customs damage Danny deeply depth discussion doll donkey Egypt Ellen essential exchange exist explanation facing film finest fireplace floating folks fort garage grabbed grandmother habit happily Harry heading hunter Illinois image independent instant January kids label Lee lungs manufacturing Martin mathematics melted memory mill mission monkey Mount mysterious neighborhood Norway nuts occasionally official ourselves palace Pennsylvania Philadelphia plates poetry policeman positive possibly practical pride promised recall relationship remarkable require rhyme rocky rubbed rush sale satellites satisfied scared selection shake shaking shallow shout silly simplest slight slip slope soap solar species spin stiff swung tales thumb tobacco toy trap treated tune University vapor vessels wealth wolf zoo".split()
   word_demo = random.choice(wordslist_demo)
   word_demo = word_demo.lower()
   word1 = word_demo
   return word1

def generate_hard_word():
    import random
    hardWords = "fizz buzz jazz quiz fox huff jiff fuzz fuzzy dizzy junk lax lox".split()
    hardWord = random.choice(hardWords)
    hardWord = hardWord.lower()
    return hardWord

def coverMystery(word_):
    mysteryWord = list("-"*len(word_))
    return mysteryWord

def uncoverLetter(letter_,wordList,coverList):
    counter = -1
    for x in wordList:
        counter += 1
        if x == letter_:
            coverList[counter] = wordList[counter]
        else:
            continue
    return coverList



def play_hangman():
   """ this is the python script version of the game """
   print("The hangman app is under construction. Try again later!")

if __name__ == '__main__':
    play_hangman()
