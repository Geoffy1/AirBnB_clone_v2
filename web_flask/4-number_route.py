#!/usr/bin/python3
"""
script start Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:              display "Hello HBNB!"
            /hbnb:          display "HBNB"
            /c/<text>:      display "C" + text (replace underscores with space)
            /python/<text>: display "Python" + text (default is "is cool")
            /number/<n>:    display "n is a number" only if int
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display txt"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display txt"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom txt given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom txt given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display txt only if int given"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
