from app import db

from sqlalchemy import Column, Integer, String

class Eisenhowers(db.Model):
    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)

    type = Column(String(100))