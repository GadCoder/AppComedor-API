from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.tickets import TicketCreate, ShowTicket
from db.session import get_db
from db.repository_tickets import create_new_ticket

router = APIRouter()


@router.post("/create-ticket/", response_model=ShowTicket)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket = create_new_ticket(ticket=ticket, db=db)
    return ticket
