#!/usr/bin/env python3
"""
Authentication module with password hashing.
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        str: The salted hash of the password.
    """
    # Convert the password to bytes and hash it
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')
