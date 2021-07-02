from flask import Blueprint, request
from app.services.category_services import create_category
bp = Blueprint("bp_category",__name__)

@bp.route("/category", methods=["POST"])
def create():
    data = request.get_json()
    print(data["name"])

    return create_category(data)