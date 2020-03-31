def generate_random_word():
   import random
   wordslist_demo = "acres adult advice arrangement attempt August Autumn border breeze brick calm canal Casey cast claws coach constantly contrast cookies customs damage Danny deeply depth discussion doll donkey Egypt Ellen essential exchange exist explanation facing film finest fireplace floating folks fort garage grabbed grandmother habit happily Harry heading hunter Illinois image independent instant January kids label Lee lungs manufacturing Martin mathematics melted memory mill mission monkey Mount mysterious neighborhood Norway nuts occasionally official ourselves palace Pennsylvania Philadelphia plates poetry policeman positive possibly practical pride promised recall relationship remarkable require rhyme rocky rubbed rush sale satellites satisfied scared selection shake shaking shallow shout silly simplest slight slip slope soap solar species spin stiff swung tales thumb tobacco toy trap treated tune University vapor vessels wealth wolf zoo".split()
   word_demo = random.choice(wordslist_demo)
   return word_demo


def initMystery(word_):
    return list("-"*len(word_))

def revMystery(letter_guess, covered_list, actual_word):
    if len(letter_guess) != 1:
        return "needOneLetter"
    elif letter_guess not in "qwertyuiopasdfghjklzxcvbnm":
        return "notInAlpha"
    elif letter_guess in guessed_letters:
        return "alreadyGuessed"
