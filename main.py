from fastapi import FastAPI, Path, HTTPException,Query

import json
app = FastAPI()

def load_data():
    f = open("patients.json", "r")
    data = json.load(f)
    f.close()
    return data


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
def view_patient(patient_id: str = Path(..., description="Id of the patient in the DB", example='P001')):
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