from flask_restful import Resource, reqparse
from models import Company
from api.company.schemas import CompanySchema

company_schema = CompanySchema()

parser = reqparse.RequestParser()
parser.add_argument("company")


class CompanyListResource(Resource):
    def get(self):
        companies = Company.get_all()
        result = company_schema.dump(companies, many=True)
        return result

    def post(self):
        args = parser.parse_args()


class CompanyDetailResource(Resource):
    def get(self, company_id):
        companies = Company.get_by_id(company_id)
        result = company_schema.dump(companies)
        return result
