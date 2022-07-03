from typing import Optional
from pydantic import BaseModel, EmailStr

"""
Campos de los platos
    id
    nombre_plato
    link_img
    puntuacion
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    img_url = Column(String)
    score = Column(Float)
"""


class DishBase(BaseModel):
    name: Optional[str] = None
    img_url: Optional[str] = None
    score: Optional[float] = None


class DishCreate(DishBase):
    name: str
    img_url: str
    score: float


class ShowDish(DishBase):
    name: str
    img_url: str
    score: float

    class Config():
        orm_mode = True

