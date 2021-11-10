#!/usr/bin/env python3
"""Session Authentication"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User



class SessionAuth(Auth):
    