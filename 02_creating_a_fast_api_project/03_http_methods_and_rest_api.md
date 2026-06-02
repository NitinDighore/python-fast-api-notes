# HTTP Methods and REST API

## What is a REST API?
REST (REpresentational State Transfer) is an architectural style used to design web services. A REST API uses standard HTTP methods to perform operations on resources (like events or users) allowing the client (browser, mobile app) and the server to communicate seamlessly.

Key terms in a REST API:
* **Resource:** The data being managed (e.g., Event, User, Registration).
* **Endpoint:** The specific URL where you access or modify the resource.
* **Method:** The HTTP action you want to perform.

## Standard HTTP Methods
* **GET:** Retrieve resource(s) from the server (e.g., fetch the entire event list).
* **POST:** Create a new resource on the server (e.g., add a new event).
* **PUT:** Replace an existing resource entirely (e.g., swap out an existing event with a new one).
* **PATCH:** Partially update a resource (e.g., change only the scheduled date of an event).
* **DELETE:** Remove an existing resource (e.g., cancel/delete an existing event).

## OpenAPI Specification
FastAPI internally uses the **OpenAPI** standard to describe your API. This widely adopted specification makes your API self-descriptive. Every route, request model, response model, and parameter you define is automatically included in the generated OpenAPI schema.

---

## Defining the Event Model (`models.py`)
To represent event details, we create an `Event` class. This defines the structure of our resource.

```python
from datetime import date

class Event:
    id: int
    title: str
    date: date
    organizer: str
    city: str
    email: str
    
    def __init__(self, id, title, date, organizer, city, email):
        self.id = id
        self.title = title
        self.date = date
        self.organizer = organizer
        self.city = city
        self.email = email

# Note: The format for the date type is "YYYY-MM-DD"
```

---

## Implementing the HTTP Methods in FastAPI (`events.py`)
Below is the complete implementation of the Event API demonstrating all standard HTTP methods. 
*(To run this, you would use: `uvicorn events:proj --reload`)*

```python
from fastapi import FastAPI, HTTPException
from typing import List
from models import Event
from datetime import date

proj = FastAPI(title="AI Event Assistant")

# Mock database using a list of Event objects
events_db: List[Event] = [
    Event(id=1, title="AI Bootcamp", date="2025-10-24", organizer="Tech Club", city="Bangalore", email="host@techclub.com"),
    Event(id=2, title="AI Webinar 2025", date="2025-11-30", organizer="XYZ Tech", city="Chennai", email="support@xyztech.com")
]

# ==========================================
# GET METHOD: Retrieve Resources
# ==========================================

@proj.get("/events")
def get_all_events():
    """Fetch all events. Returns the entire list of events from the server."""
    return events_db

@proj.get("/events/search")
def search_events(title: str, city: str = "Bangalore"):
    """
    Search events using Query Parameters.
    Checks if the 'title' is contained within the event's title, and matches the 'city'.
    """
    result = []
    for event in events_db:
        if event.title.lower().count(title.lower()) > 0 and event.city.lower() == city.lower():
            result.append(event)
            
    if len(result) > 0:
        return result
    return {"message": "No events found with title containing '" + title + "' and city as " + city}

@proj.get("/events/{event_id}")
def get_event(event_id: int):
    """Fetch a specific event using its unique event_id (Path Parameter)."""
    for event in events_db:
        if event.id == event_id:
            return {"event details": event}
    return {"message": "Event with id " + str(event_id) + " is not available."}

# ==========================================
# POST METHOD: Create a New Resource
# ==========================================

@proj.post("/events/add")
def create_event(event_id: int, title: str, date: date = date.today(), organizer: str = None, email: str = None, city: str = "Bangalore"):
    """
    Create a new event. Validates if the ID already exists to prevent duplicates.
    """
    for event in events_db:
        if event.id == event_id:
            return {"ERROR!!!": "Event ID " + str(event_id) + " already exists!!!"}
            
    event = Event(event_id, title, date, organizer, city, email)
    events_db.append(event)
    return {"message": "Event created successfully", "event": event}

# ==========================================
# PUT METHOD: Replace an Existing Resource
# ==========================================

@proj.put("/events/replace/{event_id}")
def update_event(event_id: int, title: str, date: date = date.today(), organizer: str = None, email: str = None, city: str = "Bangalore"):
    """Replace an existing event completely with a newly created Event object."""
    for i, event in enumerate(events_db):
        if event.id == event_id:
            updated_event = Event(event_id, title, date, organizer, city, email)
            events_db[i] = updated_event
            return {"message": "Event updated", "event": updated_event}
    return {"error": "Event not found"}

# ==========================================
# PATCH METHOD: Partially Update a Resource
# ==========================================

@proj.patch("/events/edit/{event_id}")
def change_event(event_id: int, title: str = None, date: date = None, organizer: str = None, city: str = None, email: str = None):
    """
    Edit specific fields of an event. Only updates fields that are explicitly provided
    (skipping fields that remain 'None').
    """
    for i, event in enumerate(events_db):
        if event.id == event_id:
            if title != None: event.title = title
            if date != None: event.date = date
            if organizer != None: event.organizer = organizer
            if city != None: event.city = city
            if email != None: event.email = email
            return {"message": "Event updated", "event": event}
    return {"error": "Event not found"}

# ==========================================
# DELETE METHOD: Remove a Resource
# ==========================================

@proj.delete("/events/cancel/{event_id}")
def delete_event(event_id: int):
    """Remove an existing event entirely from the events_db."""
    for event in events_db:
        if event.id == event_id:
            events_db.remove(event)
            return {"message": f"Event with id {event_id} deleted"}
    return {"error": "Event not found"}
```