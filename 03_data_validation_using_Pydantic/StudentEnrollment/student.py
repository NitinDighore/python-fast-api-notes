from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List
from models import Student


app = FastAPI(title="Student Enrollment")

student_db: List[Student] = [
    Student(
        id=1,
        name="ABC",
        age= 6,
        email= "abc@gmail.com"
    )
]

@app.get("/students")
def get_all_students():
    return student_db

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in student_db:
        if student.id == student_id:
            return {"student details": student}
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students/add")
def create_student(student: Student):
    for student_data in student_db:
        if student.id == student_data.id:
            raise HTTPException(status_code=400, detail="Student with this ID already exists")
    student_db.append(student)
    return {"message": "Student created successfully", "student": student}
    
    
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in student_db:
        if student.id == student_id:
            student.name = updated_student.name
            student.age = updated_student.age
            student.email = updated_student.email
            return {"message": "Student updated successfully", "student": student}
        else:
            raise HTTPException(status_code=404, detail="Student not found")
        
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in student_db:
        if student.id == student_id:
            student_db.remove(student)
            return {"message": "Student deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Student not found")


if __name__ == "__main__":
    # Starting the student app on port 8003
    uvicorn.run("student:proj", host="localhost", port=8003, reload=True)