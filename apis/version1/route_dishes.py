from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.session import get_db
from schemas.dishes import DishCreate, ShowDish
from db.repository.dishes import create_new_dish, retreive_dish, retreive_all_dishes

router = APIRouter()


"""

Aca se crean las rutas para los platos
Si se hace una peticion http a la ruta:
    -/dishes/create-dish se puede crear un plato
    -/dishes/get/{id} se recibe el plato con ese id
    -/dishes/get/all se reciben todos los platos
"""

@router.post("/create-dish/", response_model=ShowDish)
def create_dish(dish: DishCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    if current_user.is_superuser:
        dish = create_new_dish(dish=dish, db=db)
        return dish
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Usuario con codigo {current_user.code} no tiene autorizacion para crear nuevos platos"
        )


@router.get("/get/all")
def read_all_dishes(db: Session = Depends(get_db)):
    dishes = retreive_all_dishes(db)
    if not dishes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No se encuentran registros de los platos")
    return dishes


@router.get("/get/{id}", response_model=ShowDish)
def read_dish(id: int, db:Session = Depends(get_db)):
    dish = retreive_dish(id=id, db=db)
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Dish with this id {id} does not exist")
    return dish


