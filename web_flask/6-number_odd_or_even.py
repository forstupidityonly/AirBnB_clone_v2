#!/usr/bin/python3
'''Module to start Flask web app'''
from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''method that returns C followed by parameter'''
    if "_" in text:
        new = text.replace("_", " ")
        return 'C {}'.format(new)
    else:
        return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def py_route(text="is cool"):
    '''method that displays “Python”, followed by
    the value of the text'''
    if "_" in text:
        new = text.replace("_", " ")
        return 'Python {}'.format(new)
    else:
        return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    '''method that returns n is a number if int'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp_route(n):
    '''method that returns n in HTML template'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even_temp(n):
    '''method that returns n in HTML template'''
    if n % 2 == 0:
        evenOdd = 'even'
    else:
        evenOdd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenOdd=evenOdd)


if __name__ == "__main__":
    app.run(HOST, PORT)
