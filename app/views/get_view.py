from app.models.task_categories_model import Task_Categories
from flask import Blueprint,jsonify

bp = Blueprint("bp_get",__name__)

@bp.route("/")
def create():
    task = Task_Categories.query.all()

    tasks = [
        {
            "category":{
                "name":item.category_table.name,
                "description":item.category_table.description,
                "task":[
                    {
                        "name": item.task_table.name,
                        "description": item.task_table.description,
                        "priority":item.task_table.eisenhowers_table.type
                    }
                ]
            }
        }
        for item in task]

    return jsonify(tasks),200