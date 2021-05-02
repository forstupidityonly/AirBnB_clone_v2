#!/usr/bin/python3
"""flask web app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """hello_hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ c is fun """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ python is cool """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:num>', strict_slashes=False)
def it_is_a_number(num):
    """ its a num """
    return "{} is a number".format(num)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
