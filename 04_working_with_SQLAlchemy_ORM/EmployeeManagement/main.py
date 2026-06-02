import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from config import session, get_db
from models import Employee
from schema import EmployeeSchema

app = FastAPI(title='Employee Management')

@app.post("/employee")
def create_employee(employee: EmployeeSchema, db: session = Depends(get_db)):
    new_employee = Employee(**employee.__dict__)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return {"message": "Employee created successfully", "employee": new_employee}

@app.get("/employee")
def get_all_employees(db: session = Depends(get_db)):
    return db.query(Employee).all()

@app.get("/employee/salary_more_than_45000")
def get_salary_more_than_45000(db: session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.salary > 45000).order_by(Employee.salary.desc()).all()
    return {"employee details": employee}

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int, db: session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"employee details": employee}

@app.put("/employee/{emp_id}")
def update_employee(emp_id: int, employee: EmployeeSchema, db: session = Depends(get_db)):
    upd_employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not upd_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    upd_employee.emp_id = employee.emp_id
    upd_employee.emp_name = employee.emp_name
    upd_employee.designation = employee.designation
    upd_employee.salary = employee.salary
    db.commit()
    db.refresh(upd_employee)
    return {"message": "Employee updated", "employee": upd_employee}

@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int, db: session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(employee)
    db.commit()
    return {"message": f"Employee with ID {emp_id} deleted"}

@app.delete("/employee/delete_by_designation/{designation}")
def delete_employee_by_designation(designation: str, db: session = Depends(get_db)):
    deleted_count = db.query(Employee).filter(Employee.designation == designation).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="No employees found with the given designation")
    
    db.commit()
    return {"message": f"Employees with designation '{designation}' deleted"}

# @app.delete("/employee/delete_by_designation/{designation}")
# def delete_employee_by_designation(designation: str, db: session = Depends(get_db)):
#     employees = db.query(Employee).filter(Employee.designation == designation).all()
#     if not employees:
#         raise HTTPException(status_code=404, detail="No employees found with the given designation")
    
#     for employee in employees:
#         db.delete(employee)
#     db.commit()
#     return {"message": f"Employees with designation '{designation}' deleted"}

if __name__ == "__main__":
    # Starting the student app on port 8003
    uvicorn.run("main:app", host="localhost", port=8003, reload=True)