from flask import Flask, render_template, request
import sqlite3
import sys


# app config
app = Flask(__name__)

history = {'apple' : 9.0,
		    'banana' : 11,
			'orange' : 15,
			'mango' : 3.5}


# Flask Site Structure
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/product_entry', methods=['GET', 'POST'])
def entry():
	if request.method == 'GET':
		return render_template('product_entry.html')
	if request.method == 'POST':
		try:
			product = request.form.get('product')
			price = request.form.get('price')
			history[product] = price
			connection = sqlite3.connect('products.db')
			cursor = connection.cursor()
			cursor.execute('INSERT INTO product_table VALUES (NULL,?,?,NULL)', (product, price))
			connection.commit()
			return render_template('entry_success.html', product=product, price=price)
		except Exception as f:
			print(f, file=sys.stderr)
			return render_template('entry_failure.html', product=product, price=price)

			

@app.route('/product_search', methods=['GET', 'POST'])
def search():
	try:
		if request.method == 'GET':
			search_term = request.args.get('search_term')
			radio = request.args.get('radio')
			connection = sqlite3.connect('products.db')
			cursor = connection.cursor()
			if radio == 'name':
				cursor.execute("SELECT Price from product_table WHERE Product = ? ", (search_term,))
			if radio == 'price':
				cursor.execute("SELECT Product from product_table WHERE Price = ? ", (search_term,))	
			result = cursor.fetchone()[0]
			return render_template ("search_success.html", result=result)
		if request.method == 'POST':
			return render_template ("product_search.html")
	except Exception as e:
		print(e, file=sys.stderr)
		return render_template ("product_search.html")


@app.route('/readme')
def readme():
	return render_template('readme.html')

@app.route('/entry_success')
def entry_success():
	return render_template('entry_success.html')

@app.route('/entry_failure')
def entry_failure():
	return render_template('entry_failure.html')

@app.route('/search_success')
def search_success():
	return render_template('search_success.html')

@app.route('/search_failure')
def search_failure():
	return render_template('search_failure.html')

@app.route('/update_delete')
def update_delete():
		return render_template('update_delete.html', history=history)

@app.route('/deleter', methods=['GET', 'POST'])
def delete():
	if request.method == 'GET':
		return render_template('deleter.html')
	if request.method == 'POST':
		return render_template('deleter.html')


@app.route('/updater', methods=['GET', 'POST'])
def update():
	if request.method == 'GET':
		return render_template('updater.html')
	if request.method == 'POST':
		return render_template('updater.html')

# @app.route('/subscribe')
# def subscribe():
# 	return render_template('subscribe.html')

# subscribers = []
# @app.route('/form', methods=['POST'])
# def form():
# 	first_name = request.form.get('first_name')
# 	last_name = request.form.get('last_name')
# 	email = request.form.get('email')

# # capture page if the form is incomplete
# 	if not first_name or not last_name or not email:
# 		error_statement = 'All form fields required...'
# 		return render_template('subscribe.html', 
# 			error_statement=error_statement, 
# 			first_name=first_name, 
# 			last_name=last_name, 
# 			email=email)

# # form collection
# 	subscribers.append(f'{first_name}{last_name}{email}')
# 	return render_template('form.html', 
# 		subscribers=subscribers, 
# 		first_name=first_name, 
# 		last_name=last_name, 
# 		email=email)



if __name__ == '__main__':
	app.run()