from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from models import (
    Company,
    Food,
    Ingredients,
    UnitOfMeasure,
    NutritionAttribute,
)
from core import app

# Flask and Flask-SQLAlchemy initialization here
db = SQLAlchemy(app)

admin = Admin(app, name="Nutritional Centro America", template_mode="bootstrap3")
admin.add_view(ModelView(Company, db.session))
admin.add_view(ModelView(Ingredients, db.session))
admin.add_view(ModelView(UnitOfMeasure, db.session))
admin.add_view(ModelView(NutritionAttribute, db.session))


class FoodModelView(ModelView):
    pass


admin.add_view(FoodModelView(Food, db.session))
