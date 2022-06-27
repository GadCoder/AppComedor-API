from sqlalchemy import Column, String, Integer, Float
from db.base_class import Base

"""
Campos de los platos
id
nombre_plato
link_img
puntuacion
"""


class Dish(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    img_url = Column(String)
    score = Column(Float)

