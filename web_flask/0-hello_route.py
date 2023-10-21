#!/usr/bin/python3
"""script that starts  a Flask web application"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """define the route for homepage"""
    return render_template("5-number.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
