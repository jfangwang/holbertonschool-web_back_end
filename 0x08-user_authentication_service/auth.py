#!/usr/bin/env python3
"""Authentication"""
import bcrypt
from sqlalchemy.ext.declarative import declarative_base
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from db import DB


def _hash_password(password: str) -> str:
    """password string arguments and returns bytes"""
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Returns the user if user credentials do not match other user's
        credentials, otherwise raises an error"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            """User does not exist, addd the user"""
            pas = _hash_password(password)
            user = self._db.add_user(email, pas)
            return user
        raise ValueError("User {} already exists.".format(email))
