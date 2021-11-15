#!/usr/bin/env python3
"""Authentication"""
import bcrypt
import uuid
from sqlalchemy.ext.declarative import declarative_base
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from db import DB


def _hash_password(password: str) -> str:
    """password string arguments and returns bytes"""
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """return a string representation of a new UUID.
    Use the uuid module."""
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """ find the user corresponding to the email,
        generate a new UUID and store it in the database
        as the user’s session_id, then return the session ID."""
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, session_id=uuid)
            return uuid
        except NoResultFound:
            return None
        except Exception as e:
            return None
        return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns the corresponding User or None"""
        try:
            return self._db.find_user_by_(session_id=session_id)
        except Exception as e:
            return None

    def destroy_session(self, used_id: int) -> None:
        """updates the corresponding user’s session ID to None"""
        try:
            self._db.update_user(user_id=user_id,
                                 session_id=None)
        except Exception as e:
            return None
        return None
