import json

from sqlalchemy.orm import Session
from schemas.dishes import DishCreate
from db.models.dishes import Dish


def create_new_dish(dish: DishCreate, db:Session):
    dish_object = Dish(**dish.dict())
    db.add(dish_object)
    db.commit()
    db.refresh(dish_object)
    return dish_object


def retreive_dish(id: int, db: Session):
    item = db.query(Dish).filter(Dish.id == id).first()
    return item


def retreive_all_dishes(db: Session):
    dishes = db.query(Dish).all()
    return dishes