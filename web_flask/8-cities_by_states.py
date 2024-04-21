#!/usr/bin/python3
"""Python script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    depo = storage.all(State).values()
    return render_template("8-cities_by_states.html", depo=depo)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
