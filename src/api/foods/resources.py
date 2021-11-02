from flask_restful import Resource, reqparse

from api.foods.schemas import FoodSchema
from models import Food

food_schema = FoodSchema()

parser = reqparse.RequestParser()
parser.add_argument("food")


class FoodListResource(Resource):
    def get(self):
        companies = Food.get_all()
        result = food_schema.dump(companies, many=True)
        return result

    def post(self):
        args = parser.parse_args()


class FoodDetailResource(Resource):
    def get(self, company_id):
        companies = Food.get_by_id(company_id)
        result = food_schema.dump(companies)
        return result
