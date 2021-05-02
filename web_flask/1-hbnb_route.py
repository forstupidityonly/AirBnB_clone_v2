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


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
