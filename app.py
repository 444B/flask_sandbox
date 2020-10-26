from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'

# # Initialize the Database
# db = SQLAlchemy(app)

# # Create a db model
# class Friends(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(200), nullable=False)
# 	date_created = db.Column(db.Datetime, default=datetime.utcnow)

# # Create a function to return a string when we add something
# 	def__repr__(self):
# 		return 'Name %r' % self.id

subscribers = []

@app.route('/')
def index():
	title = '444B\'s portfolio'
	return render_template('index.html', title=title)

@app.route('/about')
def about():
	title = 'About page'
	return render_template('about.html', title=title)

@app.route('/sandbox')
def sandbox():
	title = 'Subsribe'
	names = ['john', 'mary', 'wess']
	return render_template('sandbox.html', 
		title=title, 
		names=names)

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