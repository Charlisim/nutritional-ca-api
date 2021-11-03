from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from core.db import BaseModelMixin, db


class Company(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return "%s" % self.name


food_identifier = db.Table(
    "food_identifier",
    db.Column("food_id", db.Integer, db.ForeignKey("food.id"), primary_key=True),
    db.Column("identifiers", db.String(100), primary_key=True),
    db.Column("identifier_name", db.String(100), primary_key=True),
)

food_nutrition_attributes = db.Table(
    "food_nutrition_attr",
    db.Column("food_id", db.Integer, db.ForeignKey("food.id"), primary_key=True),
    db.Column(
        "nutrition_attr_id",
        db.Integer,
        db.ForeignKey("nutrition_attribute.id"),
        primary_key=True,
    ),
    db.Column("value", db.Integer),
    db.Column("uom_id", db.Integer, db.ForeignKey("uom.id"), primary_key=True),
    db.Column("created_date", db.DateTime, default=datetime.utcnow),
)


class NutritionAttribute(db.Model, BaseModelMixin):
    __tablename__ = "nutrition_attribute"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("nutrition_attribute.id"))
    parent = db.relationship("NutritionAttribute", remote_side=[id])
    created_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self) -> str:
        return "%s" % self.name


class UnitOfMeasure(db.Model, BaseModelMixin):
    __tablename__ = "uom"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    multiplier = db.Column(db.Float, nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("uom.id"))
    parent = db.relationship("UnitOfMeasure", remote_side=[id])

    def __repr__(self) -> str:
        return "%s" % self.name


class Ingredients(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    foods = db.relationship("FoodIngredients", backref=db.backref("ingredients"))

    def __repr__(self) -> str:
        return "%s" % self.name


class FoodIngredients(db.Model, BaseModelMixin):
    __tablename__ = "food_ingredients"
    food_id = db.Column(db.Integer, db.ForeignKey("food.id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), primary_key=True)
    order = db.Column(db.String(50))


class Food(db.Model, BaseModelMixin):
    __tablename__ = "food"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=True)
    company = db.relationship("Company", backref=db.backref("foods"), lazy=True)
    ingredients = db.relationship("FoodIngredients", backref=db.backref("food"))

    def __repr__(self) -> str:
        return "%s" % self.name


if __name__ == "__main__":
    db.create_all()

    db.session.commit()
