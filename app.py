from flask import Flask, render_template, request
from datetime import datetime

# app config
app = Flask(__name__)

# Initialize the Database


subscribers = []

@app.route('/')
def index():
	title = '444B\'s portfolio'
	return render_template('index.html', title=title)

@app.route('/product_entry')
def entry():
	title = 'Product Entry Page'
	return render_template('product_entry.html', title=title)

@app.route('/product_search')
def search():
	title = 'Product Search'
	return render_template('product_search.html', title=title)

@app.route('/subscribe')
def subscribe():
	title = 'Subscribe'
	return render_template('subscribe.html', title=title)

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
