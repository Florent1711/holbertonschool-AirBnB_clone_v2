#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    # Replace underscores with spaces
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)