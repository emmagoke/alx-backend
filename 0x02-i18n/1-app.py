#!/usr/bin/env python3
"""
This is a flask app that impliments simple Internationalization
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """
    This class is used for the configuration of the flask app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Using Config class to configure this flask app
app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def home():
    """ The home route. """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
