from flask import request, Blueprint
from flask_restful import Api, Resource
from api.schemas import CompanySchema
from models import Company

company_v1_0_bp = Blueprint("company_v1_0_bp", __name__)
company_schema = CompanySchema()


class CompanyListResource(Resource):
    def get(self):
        companies = Company.get_all()
        result = company_schema.dump(companies, dump=True)
        return result


api = Api(company_v1_0_bp)
api.add_resource(
    CompanyListResource, "/api/v1.0/company/", endpoint="company_list_resource"
)
