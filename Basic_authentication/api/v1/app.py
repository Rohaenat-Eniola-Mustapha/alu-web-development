#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify
from api.v1.views.index import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.errorhandler(401)
def unauthorized_error(error):
    """Handles 401 Unauthorized errors"""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
