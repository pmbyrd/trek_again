"""
This is the users package.
Intended to contain all user-related functionality for the Trek project user blueprint.
"""

from flask import Blueprint

users = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/users'
)

from users import routes