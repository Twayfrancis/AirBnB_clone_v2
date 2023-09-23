#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """define the route for the homepage"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """define the route for /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """define the route for /c/<text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """define the route fot /python/"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_numbet(n):
    """define /number/<n>: display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
