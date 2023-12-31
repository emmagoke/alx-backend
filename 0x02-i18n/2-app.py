#!/usr/bin/env python3
"""
This is a flask app that impliments simple Internationalization
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    This class is used for the configuration of the flask app.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    This function determine the best match with local supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', )
def home() -> str:
    """ This is the home route. """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
