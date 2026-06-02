from pydantic import BaseModel, Field, EmailStr, field_validator

class Student(BaseModel):
    id: int
    name: str
    age:int=5 # Field(ge=5) "msg": "Input should be greater than or equal to 5",
    email: EmailStr
    
    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value < 5:
            raise ValueError("Age must be greater than 5")
        return value
