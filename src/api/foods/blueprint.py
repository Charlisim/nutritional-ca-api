from flask import Blueprint
from flask.helpers import url_for
from flask_restful import Api

from api.foods.resources import FoodDetailResource, FoodListResource

food_blueprint = Blueprint("food", __name__, template_folder="templates", url_prefix="/foods")
api = Api(food_blueprint)
api.add_resource(FoodListResource, "/", "list")
api.add_resource(FoodDetailResource, "/<int:company_id>", "detail")
