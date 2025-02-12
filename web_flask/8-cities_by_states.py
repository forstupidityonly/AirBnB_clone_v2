#!/usr/bin/python3
"""flask web app to fun ab&b"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """states list"""
    states_list = storage.all(State)
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def tear_down(context):
    """close"""
    storage.close()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
