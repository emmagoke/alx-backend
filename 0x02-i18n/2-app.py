#!/usr/bin/env python3
"""
This is a flask app that impliments simple Internationalization
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)

class Config(object):
    """
    This class is used for the configuration of the flask app.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector   # Accept-Languages is an Http request header
def get_locale():
    """
    This function determine the best match with local supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ This is the home route. """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
