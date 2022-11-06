from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return '<h1>HELLO {}!</h1>'.format(name)
