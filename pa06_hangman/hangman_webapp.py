"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""
from flask import Flask, render_template, request
import hangmanMethods
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
         'listword': 'interesting',
		 'word_so_far':"-----------",
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def start():
	global state
	state['word']=hangmanMethods.generate_random_word()
	state['listword'] = hangmanMethods.listoriginalWord(state['word'])
	state['guesses'] = []
	state['word_so_far'] = hangmanMethods.coverMystery(state['word'])
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
	       return start()

	elif request.method == 'POST':
		letter = request.form['guess']
		playerguess = hangmanMethods.guessMystery(letter, state['word_so_far'], state['listword'])
		if playerguess == "needOneLetter":
			guessresult = "needOneLetter"
		elif playerguess == "notInAlpha":
			guessresult = "notInAlpha"
		elif playerguess == "alreadyGuessed":
			guessresult = "alreadyGuessed"
		elif playerguess == "correctGuess":
			guessresult = "correctGuess"
			state['word_so_far'] = newWordsoFar(letter, state['word_so_far'], state['listword'])
		elif playerguess == "incorrectguess":
			state['guesses'] += [letter]
	return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
