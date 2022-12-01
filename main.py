import models
from fastapi import FastAPI
from database import SessionLocal, engine
from sqlalchemy.orm import session
from database import Base
from routers.router import router



models.Base.metadata.create_all(bind=engine)
session = SessionLocal()



app = FastAPI()
app.include_router(router)




