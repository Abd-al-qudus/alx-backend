#!/usr/bin/env python3
"""a flask app with a / route to return hello world,
    with configured available language using a config
    class"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    return render_template('3-index.html', title=_('home_title'), header=_('home_header'))


@babel.localeselector
def get_locale():
    """get user locale and translate"""
    requested_locale = request.args.get('locale')
    
    # Check if the requested_locale is a supported locale
    supported_locales = Config.LANGUAGES
    if requested_locale and requested_locale in supported_locales:
        return requested_locale
    
    # If not, fallback to the default behavior to determine the locale
    return request.accept_languages.best_match(supported_locales)


app.config.from_object(Config)
