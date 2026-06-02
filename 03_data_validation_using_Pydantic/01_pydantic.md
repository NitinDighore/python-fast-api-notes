# Pydantic Data Validation

## 1. Pydantic Basics
Pydantic provides automatic data validation for FastAPI using Python model classes.
- **Enforces type validation** at runtime.
- **Supports custom validations** (email, dates, length, etc.).
- **Returns clear error messages** (e.g., `422 Unprocessable Entity` for invalid or missing data).

---

## 2. Creating Models & Built-in Validation
Use `BaseModel` to define data schemas. By default, **all defined attributes are required**.

```python
from pydantic import BaseModel, EmailStr, Field
from datetime import date

class Event(BaseModel):
    id: int
    # Field validation: Restrict string length
    title: str = Field(min_length=2, max_length=50)
    # Date validation: Strictly enforces "YYYY-MM-DD" format
    date: date
    organizer: str
    city: str
    # Email validation: Automatically checks for valid email patterns (requires @)
    email: EmailStr
```

---

## 3. Custom Field Validators
Use the `@field_validator` decorator to implement custom business logic, such as preventing a user from setting an event date in the past.

```python
from pydantic import BaseModel, field_validator
from datetime import date

class Event(BaseModel):
    date: date
    
    @field_validator("date")
    @classmethod
    def check_future_date(cls, value):
        if value < date.today():
            raise ValueError("Event date cannot be in the past")
        return value
```

---

## 4. Manual Error Handling (`HTTPException`)
When Pydantic's automatic validation isn't enough, use FastAPI's `HTTPException` to manually enforce business rules, stop execution, and return structured HTTP responses.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Example 1: Prevent Duplicate Data (400 Bad Request)
@app.post("/events/add")
def create_event(event: Event):
    if any(e.id == event.id for e in events_db):
        raise HTTPException(status_code=400, detail="Event ID already exists")

# Example 2: Resource Not Found (404 Not Found)
@app.get("/events/{event_id}")
def get_event(event_id: int):
    raise HTTPException(status_code=404, detail="Event not found")

# Example 3: Unauthorized Access (403 Forbidden)
@app.delete("/events/{event_id}")
def delete_event(event_id: int, user_role: str = "participant"):
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="You are not allowed to delete events")
```

---

## 5. Quick Reference: HTTP Status Codes
| Status Code | Meaning | When to Use |
| :--- | :--- | :--- |
| **400** | Bad Request | Wrong input, duplicate ID, business rule violation. |
| **401** | Unauthorized | Missing or invalid credentials. |
| **403** | Forbidden | Authenticated, but lacks required permissions. |
| **404** | Not Found | Requested resource (Event/User) does not exist. |
| **409** | Conflict | Duplicate data (e.g., email or username already taken). |
| **422** | Unprocessable Entity | Pydantic validation errors (missing/invalid fields). |
| **500** | Server Error | Unexpected system failures or unhandled exceptions. |