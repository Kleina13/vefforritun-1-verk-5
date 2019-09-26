# APP

from os import urandom
from flask import Flask, render_template as rend, session

app = Flask(__name__)
app.secret_key = urandom(13)

@app.route('/')
def index():
	session['user'] = 'Palli'
	return '<h1>Velkominn</h1>'

@app.route('/get')
def get_session():
	if 'user' in session:
		return session['user']
	return 'Not logged in'

@app.route('/kill')
def kill_user_session():
	session.pop('user', None)
	return 'Killed Palli'

# error <<<<<<<<<<
@app.errorhandler(404)
def error404(error):
	return '<br><br><h1 style="text-align: center;">ERROR 404</h1><h2 style="text-align: center;">page not found<h2>'

@app.errorhandler(500)
def error500(error):
	return '<br><br><h1 style="text-align: center;">ERROR 500</h1><h2 style="text-align: center;">page not found<h2>'
# error <<<<<<<<<<

if __name__ == "__main__":
	app.run(debug=True)