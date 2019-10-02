# APP

from os import urandom
from flask import Flask, render_template as rend, session, request
# from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(13)

books = [{'id': 0, 'name': "The Anarchist Cookbook", 'value': "3400", 'img': "acb.jpg"},
		 {'id': 1, 'name': "The Communist Manifesto", 'value': "2100", 'img': "c_man.jpg"},
		 {'id': 2, 'name': "Mein Kampf", 'value': "4800", 'img': "mein_k.jpg"},
		 {'id': 3, 'name': "Quran", 'value': "2000", 'img': "Quran.jpg"},
		 {'id': 4, 'name': "Lord of the Flies", 'value': "4600", 'img': "lotf.jpg"},
		 {'id': 5, 'name': "The Gospel of the Flying Spaghetti Monster", 'value': "3700", 'img': "tgoftfsm.jpg"}]


@app.route('/')
def index():
	return rend('t.html', books=books)

@app.route('/cart')
def cart():
	if 'cart' not in session:
		return '<h2>Karfa tóm</h2><a href="/">back</a>'
	lepic = ""
	for item in session['cart']:
		lepic += " " + item
	return f'<h2>{lepic}</h2><a href="/">back</a>'

@app.route('/cart/add/<int:ID>')
def add(ID):
	if 'cart' not in session:
		session['cart'] = []
	session['cart'] += str(books[ID]['id'])
	return '<head><meta http-equiv="Refresh" content="1; url=/"></head>'

@app.route('/get')
def get_session():
	if 'cart' in session:
		return str(session['cart'])
	return 'your cart is empty'

@app.route('/clear')
def clear_cart():
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