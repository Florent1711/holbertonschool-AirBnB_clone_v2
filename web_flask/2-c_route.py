#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def custom_text(text):
    # Repalce underscores with spaces
    formatted_text = text.replace('_', ' ')
    return f"c {formatted_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
