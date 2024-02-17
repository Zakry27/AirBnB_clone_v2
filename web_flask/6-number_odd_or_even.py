#!/usr/bin/python3
"""Starts web app with two routings
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns string when route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns string when route is queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Returns reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformats text based on optional var
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allows request if path var is valid int
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieves template for the request
    """
    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Renders the template based on conditional
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
