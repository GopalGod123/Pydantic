from pydantic import BaseModel, computed_field, EmailStr
from typing import List, Dict

class Patient(BaseModel):

    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/ (self.height**2),2)
        return bmi
    

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print('BMI', patient.bmi)


patient_info= {'name':'Gopal', 'email':'gopalkhandelwal@gmail.com', 'age':27, 'weight':65.7, 'married':False,'height':1.72, 'allergies': ['lokesh se baat krna ', 'papa k samne paise ki bheek mangna'], 'contact_details': {'phone':'2143223', 'emergency':'214235432'}}


patient1 = Patient(**patient_info)
update_patient_data(patient1)