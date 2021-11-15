#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes="False")
def default():
    """return a JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes="False")
def users():
    """API endpoint for registering users"""
    user = request.form.get("email")
    pas = request.form.get("password")
    try:
        AUTH.register_user(user, pas)
        return jsonify({"email": user, "message": "user created"}), 200
    except (NoResultFound):
        return jsonify({"message": "email already registered"}), 400
    except Exception(e):
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes="False")
def login():
    """Logging in feature"""
    user = request.form.get("email")
    pas = request.form.get("password")

    if AUTH.valid_login(user, pas):
        session = AUTH.create_session(user)
        output = jsonify({"email": user, "message": "logged in"})
        output.set_cookie('session_id', session)
        return output
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes="False")
def logout():
    """Find the user with the requested session ID. If the user exists
    destroy the session and redirect the user to GET /"""
    session = request.cookies.get("session_id")
    if session is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes="False")
def profile():
    """find the user. If the user exist, respond with a 200 HTTP
    status and the following JSON payload"""
    session = request.cookies.get("session_id")
    if session is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session)
    if user is None:
        abort(403)
    return jsonify({"email": "{}".format(user.email)}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes="False")
def get_reset_password_token():
    """Logging in feature"""
    user = request.form.get("email")
    if user is None:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(user)
    except ValueError:
        abort(403)
    return jsonify({"email": user, "reset_token": token}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
