#!/usr/bin/env python3
"""
Authentication module for user management.
"""

from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
from typing import Optional
from auth import _hash_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the given email and password.

        Args:
            email (str): The email of the user.
            password (str): The user's password.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            # Check if a user with this email already exists
            self._db._session.query(User).filter_by(email=email).one()
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password
            hashed_password = _hash_password(password)

            # Create and return the new user
            return self._db.add_user(email, hashed_password)
