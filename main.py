import utils.session
from fastapi import FastAPI, Path, HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
app = FastAPI()

def load_data():
    f = open("patients.json", "r")
    data = json.load(f)
    f.close()
    return data

class Patient(BaseModel):
    id:Annotated[str, Field(...,description="Unique ID of the patient", example=["P001", "P002"])]
    name:Annotated[str, Field(..., description="Full name of the patient", example="John Doe")]
    city:Annotated[str, Field(..., description="City where the patient resides", example="New York")]
    age:Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient", example=30) ]
    gender:Annotated[Literal['male', 'female', 'other'], Field(..., description="Gender of the patient", example="male")]
    height:Annotated[float, Field(..., gt=0, description="Height of the patient in cm", example=175.5)]
    weight:Annotated[float, Field(..., gt=0, description="Weight of the patient in kg", example=70.2)]

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height/100
        bmi = self.weight / (height_in_meters ** 2)
        return round(bmi, 2)
    
    @computed_field
    @property
    def bmi_category(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= self.bmi < 24.9:
            return 'Normal weight'
        elif 25 <= self.bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obesity'      

class Patient_Update(BaseModel):
    name:Annotated[Optional[str], Field(None, description="Full name of the patient", example="John Doe")]
    city:Annotated[Optional[str], Field(None, description="City where the patient resides", example="New York")]
    age:Annotated[Optional[int], Field(None, gt=0, lt=120, description="Age of the patient", example=30) ]
    gender:Annotated[Optional[Literal['male', 'female', 'other']], Field(None, description="Gender of the patient", example="male")]
    height:Annotated[Optional[float], Field(None, gt=0, description="Height of the patient in cm", example=175.5)]
    weight:Annotated[Optional[float], Field(None, gt=0, description="Weight of the patient in kg", example=70.2)]


@app.get("/")
def hello():
    return {'message': "Patient Management System API"}


@app.get('/about')
def about():
    return {'message': "Fully functional API to manage your patient records"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="Id of the patient in the DB", examples='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

#Query Parameter

# Query parameters are optional key-value pairs appended to the end of a URL used to pass additional data to the server in an HTTP request. They are typically employed for operations like filtering, sorting searching and paginaation without altering the endpoint path itself 


# Eg:- /patients?city=Delhi&sort_by=age

@app.get('/sort')
def sort_patients(sort_by:str = Query(..., description='Sort on the basis of height, weight or bmi'), order:str = Query('asc', description='Order by Asc or Desc')):

    valid_fields = ['height', 'weight', 'bmi']
    

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order')

    data = load_data()
    sort_order = True if 'asc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)

    return sorted_data 


@app.post('/create')
def create_patient(patient:Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient with this ID already exists')
    data[patient.id] = patient.model_dump()
    with open('patients.json', 'w') as f:
        json.dump(data,f, indent=4)
    return JSONResponse(status_code=201, content={"message": "Patient record created successfully"}) 


@app.put('/update/{patient_id}')
def update_patient(patient_id: str, patient_update: Patient_Update):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient = data[patient_id]
    update_data = patient_update.model_dump(exclude_unset=True)
    update_data.pop("id", None)  # ID should not be updated
    existing_patient.update(update_data)
    existing_patient["id"] = patient_id  # Ensure id is present and correct
    patient_obj = Patient(**existing_patient)
    data[patient_id] = patient_obj.model_dump()

    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
    return {"message": "Patient record updated successfully"}

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    data.pop(patient_id)
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
    return {"message": "Patient record deleted successfully"}
    


