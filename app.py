from flask import Flask, render_template, request
import sqlite3
# import os


# currentdirectory = os.path.dirname(os.path.abspath(__file__))

# app config
app = Flask(__name__)

# Flask Site Structure
@app.route('/')
def index():
	title = '444B\'s portfolio'
	return render_template('index.html', title=title)

@app.route('/product_entry', methods=['GET', 'POST'])
def entry():
	title = 'Product Entry Page'
	if request.method == 'GET':
		name = request.form['name']
		connection = sqlite3.connect('products.db')
		cursor = connection.cursor()
		query1 = "INSERT INTO product_table VALUES('{n}', {p})".format(n = name, p = price)
		cursor.execute(query1)
		connection.commit()
		return render_template('product_entry.html')
	if request.method == 'POST':
		return render_template('product_entry.html')

@app.route('/product_search', methods=['GET', 'POST'])
def search():
	title = 'Product Search'
	try:
		if request.method == 'GET':
			name = request.args.get('Product')
			connection = sqlite3.connect('products.db')
			cursor = connection.cursor()
			query1 = "SELECT Price from product_table WHERE Product = '{n}'".format(n = name)
			result = cursor.execute(query1)
			result = result.fetchall()[0][0]
			return render_template ("product_search.html", Price = Result)
		if request.method == 'POST':
			return render_template ("product_search.html", Price = '')
	except:
			return render_template ("product_search.html", Price = '')


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