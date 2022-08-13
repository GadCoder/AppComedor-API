from typing import Optional
from pydantic import BaseModel


class TicketBase(BaseModel):
    ticket_id: Optional[str] = None
    code: Optional[str] = None
    shift: Optional[str] = None
    hour: Optional[str] = None


class TicketCreate(TicketBase):
    ticket_id: int
    code: str
    shift: str
    hour: str

class ShowTicket(TicketBase):
    code: str
    shift: str
    hour: str

    class Config():
        orm_mode = True