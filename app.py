# APP

from os import urandom
from flask import Flask, render_template as rend, session, request
# from pprint import pprint

app = Flask(__name__)
app.secret_key = urandom(13)

books = [{'id': 0, 'name': "The Anarchist Cookbook", 'value': "34.96", 'image': "acb.jpg"},
		 {'id': 1, 'name': "The Communist Manifesto", 'value': "21.96", 'image': "c_man.jpg"},
		 {'id': 2, 'name': "Mein Kampf", 'value': "48.96", 'image': "mein_k.jpg"},
		 {'id': 3, 'name': "Quran", 'value': "20.96", 'image': "Quran.jpg"},
		 {'id': 4, 'name': "Lord of the Flies", 'value': "46.96", 'image': "lotf.jpg"},
		 {'id': 5, 'name': "The Gospel of the Flying Spaghetti Monster", 'value': "9.96", 'image': "tgoftfsm.jpg"},
		 {'id': 6, 'name': "Angels of the Universe", 'value': "22.96", 'image': "aotu.jpg"},
		 {'id': 7, 'name': "The Bible", 'value': "15.96", 'image': "tb.jpg"},
		 {'id': 8, 'name': "Fifty Shades of Gray", 'value': "22.96", 'image': "fsog.jpg"},
		 {'id': 9, 'name': "The Hobbit", 'value': "37.96", 'image': "th.jpg"},
		 {'id': 10, 'name': "The Boy in Striped Pajamas", 'value': "24.96", 'image': "tbisp.jpg"},
		 {'id': 11, 'name': "The Diary of a Young Girl", 'value': "39.96", 'image': "tdoayg.jpg"},
		 {'id': 12, 'name': "Trump: The Art of the Deal", 'value': "33.96", 'image': "taotd.jpg"},
		 {'id': 13, 'name': "Ninja: Get Good: My Ultimate Guide to Gaming", 'value': "16.96", 'image': "ggmugtg.jpg"}]


@app.route('/')
def index():
	return rend('store.html', books=books)

@app.route('/cart')
def cart():
	cart, cartQuantity, price_sum = [], [], .0
	if 'cart' not in session:
		return rend('cart.html', cart="Cart empty", books=books, cartQuantity=[], price_sum=price_sum)
	for item in session['cart']:
		cart.append(int(item))
	for item in books:
		if int(item['id']) in cart:
			cartQuantity.append([item, cart.count(item['id'])])
	for item in cartQuantity:
		item.append(float(item[0]['value']) * item[1])
		price_sum += float(item[0]['value']) * item[1]
	price_sum = round(price_sum, 3)
	return rend('cart.html', cart=cart, books=books, cartQuantity=cartQuantity, price_sum=price_sum)

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

@app.route('/remove/<int:ID>')
def remove(ID):
	cart = []
	for item in session['cart']:
		cart.append(int(item))
	for item in cart:
		if item == ID:
			cart.remove(item)
			break
	session['cart'] = cart
	if len(session['cart']) == 0: 
		session.pop('cart', None)
	return '<head><meta http-equiv="Refresh" content="2; url=/cart"></head>removed item from list'

@app.route('/secret')
def secret():
	if 'cart' not in session: 
		session['cart'] = []
	for item in books: 
		session['cart'] += str(item['id'])
	return '<head><meta http-equiv="Refresh" content="0; url=/cart"></head>'

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
