from sqlalchemy.orm import Session

from schemas.tickets import TicketCreate
from db.models.tickets import Ticket

def create_new_ticket(ticket:TicketCreate, db:Session):

    ticket = Ticket(**ticket.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_number_of_tickets_from_shift(shift: str, db: Session):
    number_of_tickets = db.query(Ticket).filter(Ticket.shift == shift).count()
    return number_of_tickets


