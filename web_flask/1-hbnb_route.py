#!/usr/bin/python3
"""Starts the web app with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns a string when route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns a string when route is queried
    """
    return 'HBNB'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
