def generate_random_word():
   import random
   wordslist_demo = "acres adult advice arrangement attempt August Autumn border breeze brick calm canal Casey cast claws coach constantly contrast cookies customs damage Danny deeply depth discussion doll donkey Egypt Ellen essential exchange exist explanation facing film finest fireplace floating folks fort garage grabbed grandmother habit happily Harry heading hunter Illinois image independent instant January kids label Lee lungs manufacturing Martin mathematics melted memory mill mission monkey Mount mysterious neighborhood Norway nuts occasionally official ourselves palace Pennsylvania Philadelphia plates poetry policeman positive possibly practical pride promised recall relationship remarkable require rhyme rocky rubbed rush sale satellites satisfied scared selection shake shaking shallow shout silly simplest slight slip slope soap solar species spin stiff swung tales thumb tobacco toy trap treated tune University vapor vessels wealth wolf zoo".split()
   word_demo = random.choice(wordslist_demo)
   word_demo = word_demo.lower()
   word1 = word_demo
   return word1


def coverMystery(word):
    mysteryWord = list("-"*len(word_))
    return mysteryWordcovered

def listoriginalWord(word):
    originalWord = list(word)
    return originalWord

def guessMystery(letter_guess, covered_list, actual_word):
    if len(letter_guess) != 1:
        return "needOneLetter"
    elif letter_guess not in "qwertyuiopasdfghjklzxcvbnm":
        return "notInAlpha"
    elif letter_guess in guessed_letters:
        return "alreadyGuessed"
    elif letter_guess in actual_word:
        return "correctGuess"
    elif letter_guess not in actual_word:
        return "incorrectGuess"

def newWordsoFar(letter_guess, covered_list, actual_word):
    counter = -1
    for x in actual_word:
        counter += 1
        if x == letter_guess:
            covered_list[counter] = actual_word[counter]
    return covered_list
