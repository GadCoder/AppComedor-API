from typing import Optional
from pydantic import BaseModel

class TicketCreate(BaseModel):
    ticket_id: int
    code: str
    shift: str
    hour: str

class ShowTicket(BaseModel):
    ticket_id: int
    code: str
    shift: str
    hour: str

    class Config():
        orm_mode = True