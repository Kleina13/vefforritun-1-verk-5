# APP

from os import urandom
from flask import Flask, render_template as rend, session
# from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(13)

items = [{'id': 0, 'name': "item", 'value': "0000", 'img': "image.jpg"},
		 {'id': 1, 'name': "item", 'value': "0000", 'img': "image.jpg"},
		 {'id': 2, 'name': "item", 'value': "0000", 'img': "image.jpg"},
		 {'id': 3, 'name': "item", 'value': "0000", 'img': "image.jpg"},
		 {'id': 4, 'name': "item", 'value': "0000", 'img': "image.jpg"},
		 {'id': 5, 'name': "item", 'value': "0000", 'img': "image.jpg"}]


@app.route('/')
def index():
	session['cart'] = []
	return '<h1>Velkominn</h1><br><a href="/cart/0">add item</a>'

@app.route('/cart')
def cart():
	lepic = ""
	for item in session['cart']:
		lepic += " " + item
	return f'<h2>{lepic}</h2><a href="/">back</a>'

@app.route('/cart/<int:ID>')
def add(ID):
	session['cart'].append("item")
	return '<head><meta http-equiv="Refresh" content="1; url=/"></head>'


@app.route('/get')
def get_session():
	if 'cart' in session:
		return str(session['cart'])
	return 'your cart is empty'

@app.route('/kill')
def kill_user_session():
	session.pop('cart', None)
	return 'emptied your cart'

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