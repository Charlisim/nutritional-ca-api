from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from core import app
from models import Company, Food, Ingredients, NutritionAttribute, UnitOfMeasure

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
