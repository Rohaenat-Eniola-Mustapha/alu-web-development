#!/usr/bin/env python3
"""
User file.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

def User(Base):
    """
    Defining any number of mapped classes.

    Args:
        Base: Mapped classes.

    Returns:
        A database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return  "User(email='%s', hashed_password='%s', session_id='%s', reset_token='%s')>" % (
            self.email, self.hashed_password, self.session-id, self.reset_token
        )
        
    return
