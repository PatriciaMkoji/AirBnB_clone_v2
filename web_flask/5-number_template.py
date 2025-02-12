#!/usr/bin/python3
"""
script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """ display string """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display string """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """ display C followed by the value of the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """ display Python followed by the value of the text variable """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isnumber(n):
    """ display “n is a number” only if n is an integer """
    if isinstance(n, int):
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersntemplates(n):
    """ display a HTML page only if n is an integer."""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
