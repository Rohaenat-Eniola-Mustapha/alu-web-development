#!/usr/bin/env python3
"""
Module for the Authentication
"""
from typing import List, TypeVar


class Auth:
    """Class for managing API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication.

        Args:
            path (str): The requested path.
            excluded_paths (List[str]): A list of paths.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True
        if not excluded_paths:  # Handles None or empty list
            return True

        # Normalize path for slash tolerance
        path = path.rstrip('/')
        normalized_excluded = [p.rstrip('/') for p in excluded_paths]

        if path in normalized_excluded:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request object.
        Currently returns None.
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.
        Currently returns None.
        """
        return None
