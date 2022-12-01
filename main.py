import models
from fastapi import FastAPI
from database import SessionLocal, engine
from sqlalchemy.orm import session
from database import Base
import requests
from requests.auth import HTTPDigestAuth




app = FastAPI()

url = "http://interns.syncronik.com/api/employee/get-divisions-details"
token = 'token 8598bdb3fe30e9027b4a66a36b9775ae6333d287'
#auth = HTTPDigestAuth('alonso@mail.com', '1234')



@app.get("/count/division")
async def consume_api():
    
    headers = {'Authorization': token}
    r = requests.get(url, headers=headers)
    response = r.json()
    
    
    try :
        transform_json = r.json()
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
         

    return {'suma_sap':suma_sap, 'suma_sf':suma_sf}


@app.get("/count/subdivision/")
async def consume_api():
    
    headers = {'Authorization': token}
    r = requests.get(url, headers=headers)
    response = r.json()
    
    try :
        transform_json = r.json()
        mm = 0
        sd = 0
        abap = 0
        backend = 0
        frontend = 0
        database = 0
        devops = 0
        for employee in transform_json:
            subdivision = employee["employee_details"]["employee"]["subdivision"]["subdivision_name"]
            print(subdivision)
            if subdivision == "MM":
                mm += len(employee)
            elif subdivision == "SD":
                sd += len(employee)
            elif subdivision == "ABAP":
                abap += len(employee)
            elif subdivision == "backend":
                backend += len(employee)
            elif subdivision == "frontend":
                frontend += len(employee)
            elif subdivision == "database":
                database += len(employee)
            elif subdivision == "DevOps":
                devops += len(employee)
                      
    except :
             "usuario listo" 
    return {'suma_mm':mm, 'suma_sd':sd, 'suma_abap':abap,'suma_backend':backend,'suma_frontend':frontend,'suma_database':database,'suma_devops':devops}


models.Base.metadata.create_all(bind=engine)
session = SessionLocal()