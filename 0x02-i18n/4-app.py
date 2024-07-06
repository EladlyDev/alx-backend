#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel, gettext
from flask import Flask, render_template, request
from typing import List, Any


class Config:
    """
    Configuration class for the application.

    Attributes:
        LANGUAGES (list): List of supported languages for the application.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale() -> str:
    """
    Selects a language translation to use for the request.

    Returns:
        str: The best language translation to use for the request.
    """
    arg = request.args.get('locale')
    if (arg and arg in Config.LANGUAGES):
        return arg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> Any:
    """
    Renders the '3-index.html' template.
    """
    t = gettext('Welcome to Holberton')
    h = gettext('Hello world!')
    return render_template('4-index.html', home_title=t, home_header=h)


if __name__ == '__main__':
    app.run(debug=True)
