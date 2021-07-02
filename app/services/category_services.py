from app.models.categories_model import Categories
from app import db
from sqlalchemy.exc import IntegrityError
def create_category(data):

    new_category = Categories(**data)

    try:
        db.session.add(new_category)
        db.session.commit()

        return {
            "id":new_category.id,
            "name":new_category.name,
            "description":new_category.description
        },201
    except IntegrityError as e:
        return {"erro": f"O {new_category.name} ja existe no banco"},404