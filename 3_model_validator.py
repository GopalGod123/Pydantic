from pydantic import BaseModel, EmailStr, AnyUrl, Field ,field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 characters", examples=["Gopal", "Soumya"])]
    age:int= Field(gt=0,lt=120)
    email:EmailStr
    weight:float = Field(gt=0)
    allergies:Optional[List[str]] = None
    contact_details:Dict[str,str]
    user_website:AnyUrl
    married:Annotated[bool,Field(default=None, description="Is the patient married or not")]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls,value):

        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")
        
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details.email)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies[0])
    print(patient.contact_details)
    print('update')


patient_info = {'name': 'gopal','email':'gopal@hdfc.com', 'age': 65, 'weight': 74.32,'allergies':['pollen','dust'], 'contact_details':{ 'mob_no':'321321242', 'emergency':'21321532'}, 'user_website':'https://www.vite.com'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)