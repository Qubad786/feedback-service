from flask_httpauth import HTTPTokenAuth

from app.setup.settings import AUTH_SECRET

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    """Used to verify user's Token"""
    return token == AUTH_SECRET
