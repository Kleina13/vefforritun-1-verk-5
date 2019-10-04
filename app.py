# APP

from os import urandom
from flask import Flask, render_template as rend, session, request
# from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(13)

books = [{'id': 0, 'name': "The Anarchist Cookbook", 'value': "34.99", 'image': "acb.jpg"},
		 {'id': 1, 'name': "The Communist Manifesto", 'value': "21.99", 'image': "c_man.jpg"},
		 {'id': 2, 'name': "Mein Kampf", 'value': "48.99", 'image': "mein_k.jpg"},
		 {'id': 3, 'name': "Quran", 'value': "20.99", 'image': "Quran.jpg"},
		 {'id': 4, 'name': "Lord of the Flies", 'value': "46.99", 'image': "lotf.jpg"},
		 {'id': 5, 'name': "The Gospel of the Flying Spaghetti Monster", 'value': "37.99", 'image': "tgoftfsm.jpg"}]


@app.route('/')
def index():
	return rend('store.html', books=books)

@app.route('/cart')
def cart():
	if 'cart' not in session:
		return rend('cart.html', cart="Cart empty", books=books)
	cart = []
	for item in session['cart']:
		cart.append(int(item))
	return rend('cart.html', cart=cart, books=books)

@app.route('/cart/add/<int:ID>')
def add(ID):
	if 'cart' not in session:
		session['cart'] = []
	session['cart'] += str(books[ID]['id'])
	return f'<head><meta http-equiv="Refresh" content="0; url=/#book{ID}"></head>'

@app.route('/clear')
def clear_cart():
	session.pop('cart', None)
	return '<head><meta http-equiv="Refresh" content="2; url=/cart"></head>emptied your cart'

# useless <<<<<<<<
@app.route('/get')
def get_session():
	if 'cart' in session:
		return str(session['cart'])
	return 'your cart is empty'
# useless <<<<<<<<

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
