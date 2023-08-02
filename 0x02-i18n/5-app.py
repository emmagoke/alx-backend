#!/usr/bin/env python3
"""
This is a flask app that handles search query
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """ This function get the login in user. """
    user = request.args.get('login_as')
    if user:
        if int(user) in users:
            user_detail = users.get(int(user))
            return user_detail
    else:
        return None


@app.before_request
def before_request():
    if get_user():
        g.user = get_user
    else:
        g.user = None


@babel.localeselector
def get_locale() -> str:
    """
    This function determine the best match with local supported languages.
    """
    query = request.args.get('locale')
    if query:
        if query in app.config['LANGUAGES']:
            return query
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """ This is the home route.  """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
