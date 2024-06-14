from flask import Blueprint

users_app = Blueprint('users_app', __name__)


@users_app.route('/')
def all_users():
    return [
        dict(name="Ali", age=23, is_active=True),
        dict(name="Reza", age=12, is_active=False),
        dict(name="Mohammad", age=25, is_active=True),
        dict(name="Fatemeh", age=35, is_active=False),
        dict(name="Aliram", age=34, is_active=True),
    ]



