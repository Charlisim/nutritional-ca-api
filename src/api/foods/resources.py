import json

from flask import request
from flask_restful import Resource, reqparse

from api.foods.schemas import FoodSchema, FoodSchemaCreate, IngredientsSchema
from core.db import db
from models import Food, FoodIngredients, Ingredients

food_schema = FoodSchema()
food_schema_create = FoodSchemaCreate()
ingredient_schema = IngredientsSchema()

parser = reqparse.RequestParser()
parser.add_argument("food")


class FoodListResource(Resource):
    def get(self):
        companies = Food.get_all()
        result = food_schema.dump(companies, many=True)
        return result

    def post(self):
        args = request.get_json()

        print(args)

        f_object = food_schema_create.loads(json.dumps(args))
        print(f_object)
        ingredients = f_object["ingredients"]
        print(ingredients)
        del f_object["ingredients"]
        food = Food(**f_object)
        food.save()

        for ingredient in ingredients:
            food_ingredients = FoodIngredients(
                ingredient_id=ingredient["id"], food_id=food.id, order=ingredient["order"]
            )
            food_ingredients.save()

        f = Food.get_by_id(food.id)
        return food_schema.dump(f), 201


class FoodDetailResource(Resource):
    def get(self, company_id):
        companies = Food.get_by_id(company_id)
        result = food_schema.dump(companies)
        return result
