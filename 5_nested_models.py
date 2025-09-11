from pydantic import BaseModel


class Address(BaseModel):

    city:str
    state:str
    pin:str

class Patient(BaseModel):
    
    name:str
    gender:str
    age:int
    address:Address


address_dict={'city': 'Chandigarh', 'state':'Punjab', 'pin':'32342'}
address1 = Address(**address_dict)

patient_dict= {'name':'gopal', 'gender':'male', 'age':27, 'address':address1}
patient1 = Patient(**patient_dict)

print(patient1.address.city)
print(patient1.address.pin)
print(patient1.address.state)
print(patient1)


# Better Organization of related data (e.g, vitals, address, insurance)
#Reusability: Use vitals in multiple models
# Readability: Easier for developers and API consumers to understand
# Validations: Nested models are validated automatically- no extra work needed