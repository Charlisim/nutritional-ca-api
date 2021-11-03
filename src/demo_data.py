from core.db import db
from core import app
from models import Company, Ingredients, NutritionAttribute, UnitOfMeasure

with app.app_context():
    g, created = UnitOfMeasure.get_or_create(name="g")
    kg, created = UnitOfMeasure.get_or_create(name="kg", parent=g, multiplier=1000)
    maravilla, created = Company.get_or_create(name="Alimentos Maravilla SA")
    soya, created = Ingredients.get_or_create(name="Soya")
    salsa_de_soya, created = Ingredients.get_or_create(name="Salsa de Soya")
    tomate, created = Ingredients.get_or_create(name="Tomate")
    azucar, created = Ingredients.get_or_create(name="Azucar")
    kcal, created = NutritionAttribute.get_or_create(name="kcal")
    hierro, created = NutritionAttribute.get_or_create(name="Hierro")
    calcio, created = NutritionAttribute.get_or_create(name="Calcio")
    proteina, created = NutritionAttribute.get_or_create(name="Proteina")
    grasa, created = NutritionAttribute.get_or_create(name="Grasas")
    grasa_trans, created = NutritionAttribute.get_or_create(
        name="Grasas trans", parent=grasa
    )
    grasa_saturada, created = NutritionAttribute.get_or_create(
        name="Grasas saturadas", parent=grasa
    )
