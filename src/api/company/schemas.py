from marshmallow import fields

from core.ext import ma


class CompanySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name")
