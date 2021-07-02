from app.services.task_category_services import create_task_category
from flask import Blueprint, request

bp = Blueprint("bp_task_category", __name__)

@bp.route("/task_category", methods=["POST"])
def create():
    data = request.get_json()

    return create_task_category(data),200