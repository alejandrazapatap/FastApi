import models
from fastapi import FastAPI, Request
from database import SessionLocal, engine
from sqlalchemy.orm import session
from database import Base
import models
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

url = "http://interns.syncronik.com/auth/login/"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")

async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type": "Bearer"}

@app.get("/user/profilepic")
async def profile_pic(token: str = Depends(oauth2_scheme)):
    print(token)
    return "usuario creado"

@app.get("/count/")
async def consume_api():
    response = Request.get("http://interns.syncronik.com/API/employee/get-divisions-details")
    return response


""" 
    
try :
    transform_json = response.json()
    suma_sap = 0
    suma_sf = 0
    for employee in transform_json:
        division = employee["employee_details"]["employee"]["division"]["division_name"]
        if division == "SAP":
            suma_sap += len(employee)
        elif division == "Software Factory":
            suma_sf += len(employee)
except :
         "usuario listo" 
 """

models.Base.metadata.create_all(bind=engine)
session = SessionLocal()
