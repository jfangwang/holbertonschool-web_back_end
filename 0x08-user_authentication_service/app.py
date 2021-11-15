#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, jsonify
from auth import Auth
app = Flask(__name__)
auth = Auth()


@app.route("/", methods=["GET"], strict_slashes="False")
def default():
    """return a JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
