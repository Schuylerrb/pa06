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

@app.route('/start')
def play():
	global state
	state = {'guesses':[],
			 'word':[],
			 'word_so_far':[],
			 'done':False,
			 'error':"",
			 'guessesLeft': 2,
			 'won': False
			 }
	newWord = hangman_app.generate_random_word()
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
				state['error'] = "game is over, type 'again' to play again, if u dont want to get out"
				return render_template('play.html',state=state)
		elif state['done'] == True and state['won'] == True:
			if letter == "again":
				return play()
			else:
				state['error'] = "you won, type 'again' in form to play again, if not get out"
				return render_template('play.html',state=state)
		if letter in state['guesses']:
			state['error'] = "chose a new letter"
		elif len(letter) != 1:
			state['error'] = "Please guess 1 letter"
		elif letter not in "qwertyuiopasdfghjklzxcvbnm":
			state['error'] = "Please guess a letter"
		else:
			state['guesses'] += [letter]
			state['guessesLeft'] -= 1
			print(state)
			print(state['word_so_far'] != state['word'])
			if (state['guessesLeft'] == 0 and state['word_so_far'] != state['word']):
				state['done'] = True
				state['error'] = "you lost sorry. the word was : " , state['word'] , " if you wish to play again simply type 'again' in the form"

				#if len(letter) != 1:
					#state['error'] = "Please guess 1 letter"
				#elif letter not in "qwertyuiopasdfghjklzxcvbnm":
					#state['error'] = "Please guess a letter"
			elif letter in state['word']:
				state['word_so_far'] = hangman_app.uncoverLetter(letter,state['word'],state['word_so_far'])
				state['error'] = "Congrats"
				state['guessesLeft'] += 1
				if (state['guessesLeft'] >= 0 and state['word_so_far'] == state['word']):
					state['done'] = True
					state['won'] = True
					state['error'] = "you have won! to play again type 'again' in the form"
			else:
				state['error'] = "Try again"


		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them

		return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
