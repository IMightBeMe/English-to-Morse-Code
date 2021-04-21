from flask import Flask, render_template, request

app = Flask(__name__)
morse = {
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
	'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
	'6': '-....', '7': '--...', '8': '---..', '9': '----.',
	'&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
	':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
	'-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
	res = ''
	string = request.form['text']

	if string == '':
		message = '<p>Please Enter English</p>'
	else:
		lst = [char for char in string]

		for i in lst:
			if i == ' ':
				res = res + '  '
			else:
				mrs = morse[i.upper()]
				res = f'{res} {mrs}'

		print(string)

		message = f'<h4>{string} in morse code is: {res}</h4>'

	return render_template('index.html', message=str(message))

@app.errorhandler(404)
def four04(e):
	return render_template('404.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
