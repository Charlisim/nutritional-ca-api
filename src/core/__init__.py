import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
from api.blueprint import api as api_blueprint

app = Flask(__name__)
app.debug = True
app.register_blueprint(api_blueprint)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_SWATCH"] = "flatly"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.url_map.strict_slashes = False

from admin_views import *


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
