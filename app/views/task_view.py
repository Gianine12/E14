from app.services.task_services import create_task
from flask import Blueprint,request

from app.models.task_model import Task

bp = Blueprint("bp_task",__name__)

@bp.route("/task", methods=["POST"])
def create():
    data = request.get_json()
    
    return create_task(data)