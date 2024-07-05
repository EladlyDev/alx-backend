#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel
from flask import Flask, render_template
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

babel = Babel(app)


@app.route('/')
def index() -> Any:
    """
    Renders the '0-index.html' template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
