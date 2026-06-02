from pydantic import BaseModel, EmailStr, field_validator
from datetime import date

class EventSchema(BaseModel):
    id: int
    title: str
    description: str
    date: date
    organizer: str
    city: str
    email: EmailStr
    venue: str
    category: str = 'tech'
    participants: int = 0
    
    @field_validator('category')
    def validate_category(cls, value):
        allowed_categories =['tech','music','business']
        if value not in allowed_categories:
            raise ValueError(f"Invalid category. Category must be one of these {allowed_categories}")
        return value