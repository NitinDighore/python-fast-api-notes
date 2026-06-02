from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date

class Event(BaseModel):
    id: int
    title: str = Field(min_length=2, max_length=20) # "msg": "String should have at least 2 characters" // "msg": "String should have at most 20 characters"
    event_name: str # Field(min_length=5) "msg": "String should have at least 5 characters",
    date: date
    organizer: str
    city: str
    email: EmailStr
    num_seats_available: int = 10 # Field(ge=10) "msg": "Input should be greater than or equal to 10"
    category: str = "Tech"
    
    @field_validator("date")      # field validator for event date
    @classmethod
    def check_future_date(cls, value):
        if value < date.today():
            raise ValueError("Event date cannot be in the past")
        return value
    
    @field_validator("num_seats_available")
    @classmethod
    def check_seats(cls, value):
        if value < 10:
            raise ValueError("Number of seats must be at least 10")
        return value
    
    @field_validator("category")
    @classmethod
    def check_category(cls, value):
        allowed_categories = ["Tech", "Music", "Art"]
        if value not in allowed_categories:
            raise ValueError(f"Category must be one of {allowed_categories}")
        return value

    @field_validator("event_name")
    @classmethod
    def check_event_name(cls, value):
        if len(value) < 5:
            raise ValueError("Event name must be at least 5 characters long")
        return value
