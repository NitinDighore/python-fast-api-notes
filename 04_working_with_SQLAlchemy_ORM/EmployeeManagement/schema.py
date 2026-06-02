from pydantic import BaseModel

class EmployeeSchema(BaseModel):
    emp_id: int
    emp_name: str
    designation: str
    salary: int