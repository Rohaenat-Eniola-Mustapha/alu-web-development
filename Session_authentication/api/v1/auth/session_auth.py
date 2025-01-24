#!/usr/bin/env python3
"""
Module for the Authentication.
"""
import base64
import uuid
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    Class for managing Session API authentication.
    """
    pass
