from marshmallow import fields

from api.company.schemas import CompanySchema
from core.ext import ma


class IngredientsSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
        )


class FoodIngredientsCreateSchema(ma.Schema):
    class Meta:
        fields = ("ingredients", "order")

    ingredients = fields.Nested(IngredientsSchema())


class FoodSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "ingredients", "company")

    ingredients = fields.Nested(
        lambda: FoodIngredientsCreateSchema(only=("ingredients.name", "order")), many=True
    )
    company = fields.Nested(CompanySchema())


class FoodSchemaCreate(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "ingredients", "company_id")
