from sqlalchemy.orm import Session
from schemas.tickets import TicketCreate
from db.models.tickets import Ticket

def create_new_ticket(ticket: TicketCreate, db:Session):
    ticket_object = Ticket(**ticket.dict())
    db.add(ticket_object)
    db.commit()
    db.refresh(ticket_object)
    return  ticket_object

def retreaive_ticket(id: int, db: Session):
    ticket = db.query(Ticket).filter(Ticket.id == id).first()
    return ticket

def retreive_all_tickets(db: Session):
    tickets=db.query(Ticket).all()
    return tickets