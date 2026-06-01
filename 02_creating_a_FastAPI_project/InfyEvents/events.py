from fastapi import FastAPI, HTTPException
import uvicorn
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

@proj.get("/events/filter")
def filter_events(year: int, month: int):
    """
    Filters events by both year and month (Query Parameters).
    Example URL: /events/filter?year=2025&month=10
    """
    result = []
    for event in events_db:
        # str() ensures we can safely parse whether it is a string or a datetime.date object
        if str(event.date).startswith(f"{year}-{month:02d}"):
            result.append(event)
            
    if len(result) > 0:
        return result
    return {"message": f"No events found for {month:02d}/{year}"}

@proj.get("/events/{event_id}")
def get_event(event_id: int):
    """Fetch a specific event using its unique event_id (Path Parameter)."""
    for event in events_db:
        if event.id == event_id:
            return {"event details": event}
    return {"message": "Event with id " + str(event_id) + " is not available."}

@proj.get("/events/{city}")
def get_events_by_city(city: str):
    """Returns events happening only in the specified city (Path Parameter)."""
    result = []
    for event in events_db:
        if event.city.lower() == city.lower():
            result.append(event)
            
    if len(result) > 0:
        return result
    return {"message": f"No events found in {city}"}

@proj.get("/events/{year}/{city}")
def get_event_count_by_year_and_city(year: int, city: str):
    """Returns a custom message with the count of events in a city for a given year."""
    count = 0
    for event in events_db:
        if str(event.date).startswith(str(year)) and event.city.lower() == city.lower():
            count += 1
    return f"{count} events found in {city} for {year}"

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

if __name__ == "__main__":
    # Starting the events app on port 8003
    uvicorn.run("events:proj", host="localhost", port=8003, reload=True)