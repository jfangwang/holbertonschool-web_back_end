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

    def valid_login(self, email: str, password: str) -> bool:
        """Try locating the user by email. If it exists, check the
        password with bcrypt.checkpw. If it matches return True. In
        any other case, return False."""
        try:
            user = self._db.find_user_by(email=email)
            pas = password.encode('utf-8')
            return bcrypt.checkpw(password=pas,
                                  hashed_password=user.hashed_password)
        except NoResultFound:
            return False
        except Exception as e:
            return False
        return False
