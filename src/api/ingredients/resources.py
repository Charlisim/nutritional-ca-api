from api.ingredients.schemas import IngredientsSchema
from flask_restful import Resource, reqparse
from models import Ingredients

ingredients_schema = IngredientsSchema()

parser = reqparse.RequestParser()
parser.add_argument("ingredient")


class IngredientsListResource(Resource):
    def get(self):
        companies = Ingredients.get_all()
        result = ingredients_schema.dump(companies, many=True)
        return result

    def post(self):
        args = parser.parse_args()


class IngredientsDetailResource(Resource):
    def get(self, company_id):
        companies = Ingredients.get_by_id(company_id)
        result = ingredients_schema.dump(companies)
        return result
