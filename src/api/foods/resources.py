import json

from flask import request
from flask_restful import Resource, reqparse

from api.foods.schemas import FoodSchema, FoodSchemaCreate, IngredientsSchema
from core.db import db
from models import Food, FoodIngredients, Ingredients, NutritionAttribute

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
        nutrition_facts = f_object["nutrition_facts"]
        print(ingredients)
        del f_object["ingredients"]
        del f_object["nutrition_facts"]

        food = Food(**f_object)
        food.save()

        for ingredient in ingredients:
            order = ingredient["order"]
            if not "id" in ingredient:
                results_by_name = Ingredients.simple_filter(name=ingredient["name"])
                if len(results_by_name) > 0:
                    ingredient = results_by_name[0]
                else:
                    ingredient = Ingredients(name=ingredient["name"])
                    ingredient.save()
            else:
                ingredient = Ingredients.get_by_id(id=ingredient["id"])
            food_ingredients = FoodIngredients(
                ingredient_id=ingredient.id, food_id=food.id, order=order
            )
            food_ingredients.save()

        for nfact in nutrition_facts:
            if not "id" in nfact:
                results_by_name = NutritionAttribute.simple_filter(name=nfact["name"])
                if len(results_by_name) > 0:
                    nutrition_attr = results_by_name[0]
                else:
                    nutrition_attr = NutritionAttribute(name=ingredient["name"])
                    nutrition_attr.save()
            else:
                ingredient = Ingredients.get_by_id(id=ingredient["id"])
            food_ingredients = FoodIngredients(
                ingredient_id=ingredient.id, food_id=food.id, order=order
            )
            food_ingredients.save()

        f = Food.get_by_id(food.id)
        return food_schema.dump(f), 201


class FoodDetailResource(Resource):
    def get(self, company_id):
        companies = Food.get_by_id(company_id)
        result = food_schema.dump(companies)
        return result
