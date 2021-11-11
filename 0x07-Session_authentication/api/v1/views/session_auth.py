#!/usr/bin/env python3
""" session auth
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Post /api/v1/auth_session/login
    Return:
      - submit email and password
    """
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if user == []:
        return jsonify({"error": "no user found for this email"}), 404
    if user[0].is_valid_password(password):
        """if password is correct with email"""
        from api.v1.app import auth
        ses_id = auth.create_session(user[0].id)
        user_info = user[0].to_json()
        user_info = jsonify(user_info)
        user_info.set_cookie(getenv("SESSION_NAME"), ses_id)
        return user_info
    else:
        return jsonify({"error": "wrong password"}), 401

@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Delete /api/v1/auth_session/logout
    Return:
      - Logout and delete session
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        return abort(404)