from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from db.session import get_db
from schemas.tickets import TicketCreate, ShowTicket
from db.repository.tickets import create_new_ticket, retreaive_ticket, retreive_all_tickets

router = APIRouter()

@router.post("/create-ticket/", response_model=ShowTicket)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    ticket = create_new_ticket(ticket = ticket, db = db)
    return ticket

@router.get("/get/all", response_model=ShowTicket)
def read_all_tickets(db: Session = Depends(get_db)):
    tickets = retreive_all_tickets(db)
    if not tickets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encuentran los tickets")
    return tickets

@router.get("/get/{id}", response_model=ShowTicket)
def read_ticket(id: int, db: Session = Depends(get_db)):
    ticket=retreaive_ticket(id = id, db = db)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ticket con id {id} no existe")
    return ticket
