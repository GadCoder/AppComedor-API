from sqlalchemy import  Column, Integer, Boolean, String
from db.base_class import Base

class Ticket(Base):
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer)
    code = Column(String)
    shift = Column(String)
    hour = Column(String)
    is_scanned = Column(Boolean)