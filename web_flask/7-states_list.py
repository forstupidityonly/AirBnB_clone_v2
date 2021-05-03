#!/usr/bin/python3
"""flask web app to fun ab&b"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
from models import storage
from models.state import State

@app.route('/states_list')
def states_list():
    """states list"""
    states_list = storage.all("State").values()
    for i in state_list:
        if isinstance(i, State):
            i = state.to_dict()
        return render_template("7-states_list.html", states=state_list)

@app.teardown_appcontext
def tear_down():
    """close"""
    storage.close()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
