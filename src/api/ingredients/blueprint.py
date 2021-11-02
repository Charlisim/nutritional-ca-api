from flask import Blueprint
from flask.helpers import url_for
from flask_restful import Api

from api.ingredients.resources import IngredientsDetailResource, IngredientsListResource

ingredients_blueprint = Blueprint(
    "ingredients", __name__, template_folder="templates", url_prefix="/ingredients"
)
api = Api(ingredients_blueprint)
api.add_resource(IngredientsListResource, "/", "list")
api.add_resource(IngredientsDetailResource, "/<int:company_id>", "detail")
