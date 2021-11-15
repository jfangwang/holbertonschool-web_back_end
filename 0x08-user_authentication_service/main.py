#!/usr/bin/env python3
"""
Main file
Unit test file making sure all functions are behaving correctly
"""
import requests


def register_user(email: str, password: str) -> None:
    """Test register user"""


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login wrong password"""


def log_in(email: str, password: str) -> str:
    """test log in"""


def profile_unlogged() -> None:
    """test progile unlogged"""


def profile_logged(session_id: str) -> None:
    """Test profile logged"""


def log_out(session_id: str) -> None:
    """test log out"""


def reset_password_token(email: str) -> str:
    """Test Reset password token"""


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test update password"""
