from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI(title="Request and Response Models API")

# ==========================================
# RESPONSE MODELS
# ==========================================

# 1. JSON Response (Default)
@app.get("/event_info")
def event_info():
    """Returns a default JSON response."""
    return {
        "name": "AI Bootcamp",
        "date": "2025-10-10",
        "organizer": "Tech Club",
        "city": "Bangalore"
    }

# 2. Plain Text Response
@app.get("/event_info_text", response_class=PlainTextResponse)
def event_info_text():
    """Returns a plain text response."""
    return "AI Bootcamp on 2025-10-10 organized by Tech Club in Bangalore"

# ==========================================
# REQUEST MODELS (Pydantic)
# ==========================================

class Event(BaseModel):
    id: int
    title: str
    organizer: str
    city: str
    email: EmailStr
    date: str

@app.post("/events/add")
def create_event(event: Event):
    """
    Expects an Event JSON object in the request body.
    FastAPI automatically validates it against the Event BaseModel.
    """
    return {"message": "Event created", "event": event}

if __name__ == "__main__":
    uvicorn.run("request_response_models:app", host="localhost", port=8005, reload=True)