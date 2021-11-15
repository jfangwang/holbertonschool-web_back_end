#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
