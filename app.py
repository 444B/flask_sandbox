from flask import Flask, render_template

app = Flask(__name__)

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
	title = 'Sandbox'
	names = ['john', 'mary', 'wess']
	return render_template('sandbox.html', title=title, names=names)