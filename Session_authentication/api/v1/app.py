#!/usr/bin/env python3
"""
Route module for the API.
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()

if AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

if AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler.

    Args:
        error: The error object.

    Returns:
        str: JSON response indicating not found error.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Unauthorized handler.

    Args:
        error: The error object.

    Returns:
        str: JSON response indicating unauthorized error.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Forbidden handler.

    Args:
        error: The error object.

    Returns:
        str: JSON response indicating forbidden error.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> None:
    """
    Before request handler to manage authentication.

    Returns:
        None: Executes request handling or raises errors.
    """
    if auth is None:
        return
    path = request.path
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/',
    ]
    if not auth.require_auth(path, excluded_paths):
        return

    # Check for both authorization header and session cookie
    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)

    # Assign the authenticated user to request.current_user
    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
