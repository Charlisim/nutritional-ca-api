from flask import Blueprint
from api.company.blueprint import company_blueprint
from api.foods.blueprint import food_blueprint
from api.ingredients.blueprint import ingredients_blueprint


api = Blueprint("api", __name__, template_folder="templates", url_prefix="/api/v1.0/")
api.register_blueprint(company_blueprint)
api.register_blueprint(food_blueprint)
api.register_blueprint(ingredients_blueprint)
