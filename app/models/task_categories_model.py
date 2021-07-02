from app import db

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

class Task_Categories(db.Model):
    __tablename__ = "task_categories"

    id = Column(Integer, primary_key=True)

    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    task_table = relationship("Task", backref=backref("task_categori_table"))
    category_table = relationship("Categories", backref=backref("categori_tasl_table"))

    