#!/usr/bin/python3
'''Module to start Flask web app'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000


@app.route('/states_list', strict_slashes=False)
def states_route():
    '''method that returns n in HTML template'''
    stateDicts = storage.all(State)

    return render_template('7-states_list.html', stateDicts=stateDicts)


@app.teardown_appcontext
def the_teardown(context):
    '''Method to remove current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(HOST, PORT)
