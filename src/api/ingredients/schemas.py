from marshmallow import fields

from core.ext import ma


class IngredientsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name")
