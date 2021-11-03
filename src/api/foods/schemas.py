from marshmallow import fields

from api.company.schemas import CompanySchema
from core.ext import ma


class IngredientsSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
        )


class NutritionAttributeSchema(ma.Schema):
    attribute_id = fields.Integer()
    attribute_name = fields.String()
    attribute_value = fields.Float()
    attribute_uom_id = fields.Integer()
    attribute_uom_name = fields.String()


class FoodIngredientsCreateSchema(ma.Schema):
    class Meta:
        fields = ("ingredients", "order")

    ingredients = fields.Nested(IngredientsSchema())


class FoodSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "ingredients", "nutrition_facts", "company")

    ingredients = fields.Nested(lambda: FoodIngredientsCreateSchema(), many=True)
    nutrition_facts = fields.Nested(lambda: NutritionAttributeSchema(), many=True)
    company = fields.Nested(CompanySchema())


class FoodSchemaCreate(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "ingredients", "company_id")
