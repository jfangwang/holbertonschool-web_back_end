#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, jsonify, request, abort
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
