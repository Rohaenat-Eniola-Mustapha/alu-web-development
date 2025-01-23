#!/usr/bin/env python3
""" Module of Index views
"""
from flask import Blueprint, abort

app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint to trigger 401 Unauthorized error"""


    abort(401)
