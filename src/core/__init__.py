import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_SWATCH"] = "flatly"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.url_map.strict_slashes = False

from admin_views import *
from api.resources import CompanyListResource


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(HelloWorld, "/")
