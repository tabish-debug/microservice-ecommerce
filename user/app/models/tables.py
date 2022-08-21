from sqlalchemy import Column, String, Integer

from app.models.connect import base

class User(base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(500), nullable=False)

