from typing import Optional
from pydantic import BaseModel

"""

class Bug(Base):
    id = Column(Integer, primary_key=True, index=True)
    day = Column(String)
    hour = Column(String)
    description = Column(String)

"""


class BugBase(BaseModel):
    day: Optional[str] = None
    hour: Optional[str] = None
    description: Optional[str] = None


class BugCreate(BugBase):
    day: str
    hour: str
    description: str


class ShowBug(BugBase):
    day: str
    hour: str
    description: str

    class Config():
        orm_mode = True
