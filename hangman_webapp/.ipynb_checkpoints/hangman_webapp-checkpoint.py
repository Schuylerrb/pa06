"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)
"""
global state
state = {'guesses':[],
		 'word':[],
		 'word_so_far':"-----------",
		 'done':False,
		 'error':"",
		 'guessesLeft':8
         }
"""
@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/start')
def play(isHard_ = False):
	#print(isHard)
	global state
	state = {'guesses':[],
			 'word':[],
			 'word_so_far':[],
			 'done':False,
			 'error':"",
			 'guessesLeft': 10,
			 'won': False,
			 'hard': False
			 }
	#global isHard
	isHard = isHard_
	if isHard == False:
		newWord = hangman_app.generate_random_word()
	else:
		newWord = hangman_app.generate_hard_word()
		state['hard'] = True
	for i in newWord:
		state['word'].append(i)
	state['guesses'] = []
	state['word_so_far'] = hangman_app.coverMystery(state['word'])
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess'].lower()
		if state['done'] == True and state['won'] == False:
			if letter == "again":
				return play()
			else:
				state['error'] = "The game is over. Type 'again' in the guess box to play again."
				return render_template('play.html',state=state)
		elif state['done'] == True and state['won'] == True:
			if letter == "again":
				return play()
			elif letter == "hard":
				#isHard = True
				#print("FINAL CHECK PASSKEY" , isHard)
				return play(True)
			else:
				state['error'] = "The game is over. Type 'again' in the guess box to play again. Or to challenge yourself type 'hard' to play against the world's hardest hangman words"
				return render_template('play.html',state=state)
		if letter in state['guesses']:
			state['error'] = "Choose a new letter."
		elif len(letter) != 1:
			state['error'] = "Please guess 1 letter."
		elif letter not in "qwertyuiopasdfghjklzxcvbnm":
			state['error'] = "Please guess a letter."
		else:
			state['guesses'] += [letter]
			state['guessesLeft'] -= 1
			print(state)
			print(state['word_so_far'] != state['word'])
				#if len(letter) != 1:
					#state['error'] = "Please guess 1 letter"
				#elif letter not in "qwertyuiopasdfghjklzxcvbnm":
					#state['error'] = "Please guess a letter"
			if letter in state['word']:
				state['word_so_far'] = hangman_app.uncoverLetter(letter,state['word'],state['word_so_far'])
				state['error'] = "Correct guess!"
				state['guessesLeft'] += 1
				if (state['guessesLeft'] >= 0 and state['word_so_far'] == state['word']):
					state['done'] = True
					state['won'] = True
					state['error'] = "Congrats! You win! Type 'again' in the guess box to play again. Or to challenge yourself type 'hard' to play against the world's hardest hangman words"
			elif (state['guessesLeft'] == 0 and state['word_so_far'] != state['word']):
				wordjoin = ""
				state['done'] = True
				if state['hard'] == True:
					state['error'] = "Sorry! You lost! The word was: " + wordjoin.join(state['word']) + ". You clearly don't have what it takes so you will have to go through easy level again. Type 'again' in the guess box to play again."
				else:
					state['error'] = "Sorry! You lost! The word was: " + wordjoin.join(state['word']) + ". Type 'again' in the guess box to play again."
			else:
				state['error'] = "Incorrect guess. Try again."


		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them

		return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
