import os
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.debug = False
ma = Marshmallow()

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_SWATCH"] = "flatly"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

from views import *
from api.resources import *
from admin_views import *
