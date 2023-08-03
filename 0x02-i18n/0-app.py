#!/usr/bin/env python3
"""a flask app with a / route to return hello world"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """return a simple welcome string"""
    return render_template('0-index.html')
