from pydantic import BaseModel
from database import Base



class ItemBase(BaseModel):
    id: str
    name: str
    email: str
    phone: str