#!/usr/bin/env python3
"""Session Authentication"""
from flask import request
from typing import List, TypeVar


class SessionAuth(Auth):
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path is valid"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path = path + '/'
        for p in excluded_paths:
            if "*" in p:
                if p[:-1] in path:
                    return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the flask request object"""
        if request is None:
            return None
        if request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the flask request object"""
        return None
