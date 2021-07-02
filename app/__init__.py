from app import views
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

db = SQLAlchemy()
mg = Migrate()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://gianine:12345@localhost:5432/e14'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.models.eisenhowers_model import Eisenhowers
    from app.models.task_model import Task
    from app.models.task_categories_model import Task_Categories
    from app.models.categories_model import Categories

    mg.init_app(app, db)

    views.init_app(app)

    return app