from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
	icone = url_for('static', filename='images/arvore.png')
	return render_template('index.html',icone=icone)