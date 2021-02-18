from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)


def make_bold(function):
    def wrapper():
        bold = function()
        return f"<b>{bold}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        emphasis = function()
        return f"<em>{emphasis}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        underlined = function()
        return f"<u>{underlined}</u>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/3nbxypT20Ulmo/giphy.gif">'


# Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return 'Bye World'


# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there, {name}, you are {number} years old"


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
