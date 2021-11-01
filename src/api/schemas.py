from core import ma
from marshmallow import fields


class CompanySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
