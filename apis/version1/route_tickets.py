from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.tickets import TicketCreate
from db.session import get_db
from db.repository.tickets import create_new_ticket

router = APIRouter()


@router.post("/create-ticket/")
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket = create_new_ticket(ticket=ticket, db=db)
    return ticket
