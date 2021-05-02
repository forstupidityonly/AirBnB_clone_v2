#!/usr/bin/python3
"""flask web app"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num):
    """ number template """
    return render_template("5-number.html", num=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def number_odd_or_even(num):
    """number odd or even"""
    if num % 2 == 0:
        div = "even"
    else:
        div = "odd"
    return render_template("6-number_odd_or_even.html", num=num, div=div)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
