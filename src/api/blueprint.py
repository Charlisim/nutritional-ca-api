from flask import Blueprint
from api.company.blueprint import company_blueprint

api = Blueprint("api", __name__, template_folder="templates", url_prefix="/api/v1.0/")
api.register_blueprint(company_blueprint)
