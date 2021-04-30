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


@app.route('/c/<size>', strict_slashes=False)
def c_route(size):
    '''method that returns C followed by parameter'''
    if "_" in size:
        new = size.replace("_", " ")
        return 'C {}'.format(new)


if __name__ == "__main__":
    app.run(HOST, PORT)
