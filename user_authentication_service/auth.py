#!/usr/bin/env python3
"""
Authentication module
"""
import uuid
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to manage authentication"""

    def __init__(self):
        """Initialize the Auth class with a database instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user with a hashed password"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()
                )
            user = self._db.add_user(email=email, hashed_password=hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user credentials"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
        except NoResultFound:
            return False
        return False


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation"""
    return str(uuid.uuid4())
