from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from db.models.dishes import Dish
from schemas.dishes import DishCreate, ShowDish
from db.repository.dishes import create_new_dish, retreive_dish

router = APIRouter()


@router.post("/create-dish/", response_model=ShowDish)
def create_dish(dish: DishCreate, db: Session = Depends(get_db)):
    dish = create_new_dish(dish=dish, db=db)
    return dish


@router.get("/get/{id}", response_model=ShowDish)
def read_dish(id:int, db:Session = Depends(get_db)):
    dish = retreive_dish(id=id, db=db)
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Dish with this id {id} does not exist")
    return dish