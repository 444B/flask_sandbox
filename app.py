from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def indef():
	title = '444B\'s portfolio'
	return render_template('index.html', title=title)

@app.route('/about')
def about():
	names = ['john', 'mary', 'wess']
	return render_template('about.html', names=names)