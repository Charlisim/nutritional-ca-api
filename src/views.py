from core import app
from models import Food
from flask import render_template


@app.route("/")
def index():
    food = Food.query.all()
    return render_template("home.html", food=food)
