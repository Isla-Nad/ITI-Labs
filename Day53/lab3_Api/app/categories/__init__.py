
from flask import Blueprint
category_blueprint = Blueprint("category", __name__, url_prefix='/categories')
from app.categories import views