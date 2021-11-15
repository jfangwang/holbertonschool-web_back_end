#!/usr/bin/env python3
"""Authentication"""
import bcrypt
from sqlalchemy.ext.declarative import declarative_base
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> str:
    """password string arguments and returns bytes"""
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
