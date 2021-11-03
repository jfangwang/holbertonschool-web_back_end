#!/usr/bin/env python3
"""Basic Authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the base64 part of the authorization"""
