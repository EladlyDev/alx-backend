#!/usr/bin/env python3
""" basic Flask app """
from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """
    Renders the '0-index.html' template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
