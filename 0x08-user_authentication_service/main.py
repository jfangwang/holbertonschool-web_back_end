#!/usr/bin/env python3
"""
Main file
Unit test file making sure all functions are behaving correctly
"""
import requests


def register_user(email: str, password: str) -> None:
    """Test register user"""
    expect = {'email': email, 'password': password}
    request = requests.post("http://localhost:5000/users", data=expect)
    assert request.status_code == 200, "Register User Failed"
    print("Register User Passed")


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login wrong password"""
    expect = {'email': email, 'password': password + 'asdf'}
    request = requests.post("http://localhost:5000/login", data=expect)
    assert request.status_code != 200, "log in wrong password Failed"
    print("log in wrong password Passed")


def log_in(email: str, password: str) -> str:
    """test log in"""
    expect = {'email': email, 'password': password + 'asdf'}
    request = requests.post("http://localhost:5000/login", data=expect)
    assert request.status_code == 200, "log in Failed"
    print("log in Passed")


def profile_unlogged() -> None:
    """test progile unlogged"""
    expect = {'session_id': ""}
    request = requests.get("http://localhost:5000/profile", data=expect)
    assert request.status_code == 403, "Profile Unlogged Failed"
    print("Profile Unlogged Passed")


def profile_logged(session_id: str) -> None:
    """Test profile logged"""
    expect = {'session_id': session_id}
    request = requests.get("http://localhost:5000/profile", data=expect)
    assert request.status_code == 200, "profile log in Failed"
    print("profile log in Passed")


def log_out(session_id: str) -> None:
    """test log out"""
    expect = {'session_id': session_id}
    request = requests.delete("http://localhost:5000/logout", data=expect)
    assert request.status_code == 200, "log out Failed"
    print("log out Passed")


def reset_password_token(email: str) -> str:
    """Test Reset password token"""
    expect = {'email': email}
    request = requests.post("http://localhost:5000/reset_password",
                            data=expect)
    assert request.status_code == 200, "reset token Failed"
    print("reset token Passed")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test update password"""
    expect = {'email': email,
              'reset_token': reset_token,
              'new_password': new_password}
    request = requests.put("http://localhost:5000/reset_password", data=expect)
    assert request.status_code == 200, "update password Failed"
    print("update password Passed")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    # register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
