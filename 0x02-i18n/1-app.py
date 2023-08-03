#!/usr/bin/env python3
"""a flask app with a / route to return hello world,
    with configured available language using a config
    class"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """babel configuration for default language and time"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def home():
    """return a simple welcome string"""
    return render_template('1-index.html')


app.config.from_object(Config)
