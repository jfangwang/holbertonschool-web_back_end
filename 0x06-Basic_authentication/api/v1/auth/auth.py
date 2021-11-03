#!/usr/bin/env python3
"""Authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path is valid"""
        if path is None or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the flask request object"""
        if request is None:
            return None
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the flask request object"""
        if request is None:
            return None
        return request
