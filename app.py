from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Roger! It seems to be working'

@app.route('/about')
def hello_world():
    return 'About this app'