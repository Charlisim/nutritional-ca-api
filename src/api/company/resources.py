from flask_restful import Resource


class CompanyListResource(Resource):
    def get(self):
        return [{"hello": "world"}]
