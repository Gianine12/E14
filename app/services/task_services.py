import re
from app import db
from app.models.task_model import Task
from app.models.eisenhowers_model import Eisenhowers

    
def create_task(data):
    type_eisenhower = type_eisenhowers(data["importance"], data["urgency"])
    
    task = {
        "name": data["name"],
        "description": data["description"],
        "duration": data["duration"],
        "importance": data["importance"],
        "urgency": data["urgency"],
        "eisenhower_id" : type_eisenhower.id
    }

    new_task = Task(**task)

    db.session.add(new_task)
    db.session.commit()

    return {
        "name": new_task.name,
        "description": new_task.description,
        "duration": new_task.duration,
        "eisenhowers_classification" : type_eisenhower.type
    }

def type_eisenhowers(importance,urgency):

    if importance == 1:
        if urgency == 1:
            return Eisenhowers.query.get(1)
        else:
            return Eisenhowers.query.get(2)
    else:
        if urgency == 1:
            return Eisenhowers.query.get(3)
        else:
            return Eisenhowers.query.get(4)
