from flask import Flask, render_template, request
import sqlite3
import sys



# app config
app = Flask(__name__)

# Flask Site Structure
@app.route('/', methods=['GET', 'POST'])
def index():
	title = '444B\'s portfolio'
	try:
		if request.method == 'GET':
			search_term = request.args.get('search_term')
			connection = sqlite3.connect('products.db')
			cursor = connection.cursor()
			cursor.execute("SELECT Price from product_table WHERE Product = ? ", (search_term,))
			result = cursor.fetchone()[0]
			return render_template ("index.html", result=result)
		if request.method == 'POST':
			product = request.form.get('product')
			price = request.form.get('price')
			connection = sqlite3.connect('products.db')
			cursor = connection.cursor()
			cursor.execute('INSERT INTO product_table VALUES (NULL,?,?)', (product, price))
			connection.commit()
			return render_template('index.html', product=product, price=price)
	except Exception as e:
		search_term = request.args.get('search_term')
		print(e, file=sys.stderr)
		print("{n} does not exist".format(n=search_term))
		return render_template ("index.html")

	return render_template('index.html', title=title)

@app.route('/product_entry', methods=['GET', 'POST'])
def entry():
	title = 'Product Entry Page'
	if request.method == 'GET':
		return render_template('product_entry.html')
	if request.method == 'POST':
		product = request.form.get('product')
		price = request.form.get('price')
		connection = sqlite3.connect('products.db')
		cursor = connection.cursor()
		cursor.execute('INSERT INTO product_table VALUES (NULL,?,?)', (product, price))
		connection.commit()
		return render_template('product_entry.html', product=product, price=price)

@app.route('/product_search', methods=['GET', 'POST'])
def search():
	title = 'Product Search'
	try:
		if request.method == 'GET':
			name = request.args.get('name')
			connection = sqlite3.connect('products.db')
			cursor = connection.cursor()
			cursor.execute("SELECT Price from product_table WHERE Product = ? ", (name,))
			result = cursor.fetchone()[0]
			return render_template ("product_search.html", result=result)
		if request.method == 'POST':
			return render_template ("product_search.html")
	except Exception as e:
		name = request.args.get('name')
		print(e, file=sys.stderr)
		print("{n} does not exist".format(n=name))
		return render_template ("product_search.html")


@app.route('/subscribe')
def subscribe():
	title = 'Subscribe'
	return render_template('subscribe.html', title=title)

subscribers = []
@app.route('/form', methods=['POST'])
def form():
	first_name = request.form.get('first_name')
	last_name = request.form.get('last_name')
	email = request.form.get('email')

# capture page if the form is incomplete
	if not first_name or not last_name or not email:
		error_statement = 'All form fields required...'
		return render_template('subscribe.html', 
			error_statement=error_statement, 
			first_name=first_name, 
			last_name=last_name, 
			email=email)

# form collection
	subscribers.append(f'{first_name}{last_name}{email}')
	title = 'Thank you!'
	return render_template('form.html', 
		title=title, 
		subscribers=subscribers, 
		first_name=first_name, 
		last_name=last_name, 
		email=email)

if __name__ == '__main__':
	app.run()