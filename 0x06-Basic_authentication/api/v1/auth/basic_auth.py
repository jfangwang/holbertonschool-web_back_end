#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """Basic Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the base64 part of the authorization"""
        if authorization_header is None or\
            not isinstance(authorization_header, str) or\
                not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a base64 string"""
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-\
                                                                        8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """returns the user email and password from the decode method"""
        if decoded_base64_authorization_header is None or\
            not isinstance(decoded_base64_authorization_header, str) or\
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        mid = decoded_base64_authorization_header.index(":")
        return (decoded_base64_authorization_header[0:mid],
                decoded_base64_authorization_header[mid + 1:])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str) or\
                user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            all_users = User.search({'email': user_email})
            for user in all_users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
