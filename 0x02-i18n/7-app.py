#!/usr/bin/env python3
"""
This is a flask app that handles search query
"""
import pytz
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
    """ This accepts request before any function. """
    if get_user():
        g.user = get_user


@babel.localeselector
def get_locale() -> str:
    """
    This function determine the best match with local supported languages.
    """
    #  Locale from URL parameters
    query = request.args.get('locale', '')
    if query in app.config['LANGUAGES']:
        return query
    #  Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    #  Locale from request header
    header_query = request.headers.get('locale', '')
    if header_query in app.config['LANGUAGES']:
        return header_query
    #  Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ This function get the timezone. """
    timezone = request.args.get('timezone', '')
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def home() -> str:
    """ This is the home route.  """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
