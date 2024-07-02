#!/usr/bin/env python3
""" 3-app simple flask app with babel """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Config class for languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """ 3-app simple flask app """
    t = _('Welcome to Holberton')
    h = _('Hello world!')
    return render_template('3-index.html', home_header=h, home_title=t)


@babel.localeselector
def get_locale():
    """ get_locale gets the best match language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
