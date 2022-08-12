from fastapi import APIRouter

from apis.version1 import route_general_pages
from apis.version1 import route_users
from apis.version1 import route_dishes
from apis.version1 import route_login
from apis.version1 import route_bugs
from apis.version1 import route_tickets

api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_dishes.router, prefix="/dishes", tags=["dishes"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_bugs.router, prefix="/bugs", tags=["bugs"])
#api_router.include_router(route_tickets.router, prefix="/tickets", tags=["tickets"])
