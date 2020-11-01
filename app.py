from flask import Flask, render_template, request, g
import sqlite3

# app config
app = Flask(__name__)

# Database Initialise
conn = sqlite3.connect('products.db')
# create a cursor
c = conn.cursor()
# create a table
c.execute("""CREATE TABLE products (

		Product TEXT,
		Price REAL

		)""")


# conn.commit()
# conn.close()


# sqlite3/flask documentation
# DATABASE = 'products.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()




# Flask Site Structure
@app.route('/')
def index():
	title = '444B\'s portfolio'
	return render_template('index.html', title=title)

@app.route('/product_entry', methods=['POST', 'GET'])
def entry():
	title = 'Product Entry Page'
	if request.method == 'POST':
		product_name = request.form['name']
		new_product_name = products(name=product_name)

	else: 
		return render_template('product_entry.html', title=title)

@app.route('/product_search')
def search():
	title = 'Product Search'
	return render_template('product_search.html', title=title)

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
	app.run(debug = True)

