import models
from fastapi import FastAPI, Request
from database import SessionLocal, engine
from sqlalchemy.orm import session
from database import Base
import models



models.Base.metadata.create_all(bind=engine)
session = SessionLocal()

app = FastAPI()


@app.get("/data")
def ItemBase():
    return "Creado"



""" @app.get("/data")
def get_user(id:int):
    return Base.query(models.User).filter(models.User.id == id).first() """
 

