from sqlalchemy.orm import Session

from schemas.tickets import TicketCreate
from db.models.tickets import Ticket

def create_new_ticket(ticket:TicketCreate, db:Session):

    ticket = Ticket(**ticket.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
