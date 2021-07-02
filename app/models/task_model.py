from app import db
from .eisenhowers_model import Eisenhowers

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Task(db.Model):
    __tablename__ =  "task"

    id = Column(Integer,  primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(String)
    duration = Column(Integer)
    importance = Column(Integer) 
    urgency = Column(Integer)

    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.id"), nullable=False)

    eisenhowers_table = relationship("Eisenhowers", backref=backref("task_table"))
