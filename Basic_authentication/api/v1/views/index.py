#!/usr/bin/env python3
""" Module of Index views
"""
from flask import Blueprint, jsonify, abort


app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Raises a 401 Unauthorized error"""
    abort(401)
