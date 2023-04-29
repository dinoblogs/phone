from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'My Name Is Krishna Sharma'

@app.route('/about')
def about():
    return 'About'
