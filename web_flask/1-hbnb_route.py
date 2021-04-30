#!/usr/bin/python3
'''Module to start Flask web app'''
from flask import Flask

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''method that returns hello world'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''method that returns hbnb'''
    return 'HBNB'


if __name__ == "__main__":
    app.run(HOST, PORT)
