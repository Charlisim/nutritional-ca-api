from flask import Blueprint
from flask.helpers import url_for
from flask_restful import Api

from api.company.resources import CompanyDetailResource, CompanyListResource

company_blueprint = Blueprint(
    "company", __name__, template_folder="templates", url_prefix="/company"
)
api = Api(company_blueprint)
api.add_resource(CompanyListResource, "/", "list")
api.add_resource(CompanyDetailResource, "/<int:company_id>", "detail")
