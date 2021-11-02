from marshmallow import fields

from api.ingredients.schemas import IngredientsSchema
from core.ext import ma


class FoodSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "ingredients")

    ingredients = fields.Nested(IngredientsSchema(), many=True)
