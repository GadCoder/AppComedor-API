from sqlalchemy.orm import Session

from schemas.tickets import TicketCreate
from db.models.tickets import Ticket

def create_new_ticket(ticket:TicketCreate, db:Session):
    ticket = Ticket(ticket_id=ticket.ticket_id,
                  code=ticket.code,
                  shift=ticket.shift,
                  hour=ticket.hour,
                  is_scanned=False)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
