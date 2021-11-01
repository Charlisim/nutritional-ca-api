from flask import Blueprint
from flask_restful import Api
from api.company.resources import CompanyListResource

company_blueprint = Blueprint(
    "company", __name__, template_folder="templates", url_prefix="/company"
)
api = Api(company_blueprint)
api.add_resource(CompanyListResource, "/")
