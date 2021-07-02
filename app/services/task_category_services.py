from app.models.eisenhowers_model import Eisenhowers
from app.models.task_categories_model import Task_Categories
from app import db
from app.models.task_model import Task
from app.models.categories_model import Categories

def create_task_category(data):

    task = Task.query.filter_by(name=data["task_name"]).first()
    category = Categories.query.filter_by(name=data["category_name"]).first()
    eisenhower = Eisenhowers.query.get(task.eisenhower_id)

    task_cat = {
        "task_id": task.id,
        "category_id":category.id
    }

    new_task_category = Task_Categories(**task_cat)
    
    db.session.add(new_task_category)
    db.session.commit()

    return {
        "task": task.name,
        "category": category.name,
        "eisenhower_classification": eisenhower.type
    }