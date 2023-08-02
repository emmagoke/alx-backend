#!/usr/bin/env python3
"""
This is a flask app that handles search query
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    This class is used for the configuration of the flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ """
    query = request.args.get('locale')
    if query:
        if query in app.config['LANGUAGES']:
            return query
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """ """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
