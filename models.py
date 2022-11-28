from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)


  