#!/usr/bin/env python3
"""
Module for the Authentication.
"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    Class for managing Session API authentication.
    """
    # In-memory storage of Session ID to User ID mappings
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id and stores it in the dictionary.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        
        # Generate a unique Session ID using uuid4
        session_id = str(uuid.uuid4())
        
        # Store the session ID and associate it with the user_id
        self.user_id_by_session_id[session_id] = user_id
        
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the User ID based on the Session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        
        # Retrieve the user ID based on the session ID (returns None if not found)
        return self.user_id_by_session_id.get(session_id)
