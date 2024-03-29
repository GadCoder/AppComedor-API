from typing import Optional
from pydantic import BaseModel


class TicketBase(BaseModel):
    ticket_id: Optional[int] = None
    code: Optional[str] = None
    shift: Optional[str] = None
    hour: Optional[str] = None
    is_scanned: Optional[bool] = False


class TicketCreate(TicketBase):
    ticket_id: int
    code: str
    shift: str
    hour: str

class ShowTicket(TicketBase):
    code: str
    shift: str
    hour: str
    is_scanned: bool
    class Config():
        orm_mode = True

class ShowFullTicket(TicketBase):
    ticket_id: int
    code: str
    shift: str
    hour: str
    is_scanned: bool
    class Config():
        orm_mode= True