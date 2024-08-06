from werkzeug.security import generate_password_hash, check_password_hash
from infrastructure.mongo_db import get_user_by_id
from flask_login import UserMixin
from wtforms import StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm

"""
Mechanism to hash password for security.
"""


def hashPass(string):
    hash = generate_password_hash(string, method='pbkdf2', salt_length=16)
    return hash


def matchHash(hashedPass, string):
    is_match = check_password_hash(hashedPass, string)
    return is_match


""""
When user need to log in its data should be stored that this user have active login session.
That is why this is a login blueprint different from flask form for storing user data and give data by id.
It uses a function from user_database from getting data from mongodb.
"""


class User(UserMixin):
    """User blueprint storing class."""

    def __init__(self, user_id, user_name, user_mail, user_pass):
        self.id = user_id
        self.name = user_name
        self.email = user_mail
        self.password = user_pass

    @staticmethod
    def get(user_id):
        user_data = get_user_by_id(user_id)  # function to get data by id defined in user_database.
        if user_data:
            return User(user_data['id'], user_data['name'], user_data['email'], user_data['password'])
        return None


"""
Flask authentication.
"""


class RegistrationForm(FlaskForm):
    """Blueprint for signup form."""
    name = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    register = SubmitField(label='Register')


class LoginForm(FlaskForm):
    """Blueprint for login form."""
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])
