#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, abort
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(401)
def unauthorized_error(error):
    """Error handler for 401 Unauthorized"""
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port)
