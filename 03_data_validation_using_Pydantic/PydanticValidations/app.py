from fastapi import FastAPI, HTTPException
from typing import List
from models import Event

proj = FastAPI(title="AI Event Assistant")

events_db: List[Event] = [
    Event(
        id=1,
        title="AI Bootcamp",
        event_name="AI Bootcamp",
        date="2027-10-24",
        organizer="Tech Club",
        city="Bangalore",
        email="host@techclub.com",
        num_seats_available=50
        ),
    Event(
        id=2,
        title="AI Webinar 2025",
        event_name="AI Webinar",
        date="2027-11-30",
        organizer="XYZ Tech",
        city="Chennai",
        email="support@xyztech.com",
        num_seats_available=10
        )
]

@proj.get("/events")
def get_all_events():
    return events_db

@proj.get("/events/{event_id}")
def get_event(event_id: int):
    for event in events_db:
        if event.id == event_id:
            return {"event details": event}
    raise HTTPException(status_code=404, detail="Event not found")

@proj.post("/events/add")
def create_event(event: Event):
    for event_data in events_db:
        if event.id == event_data.id:
            # return {"ERROR!!!":"Event already exists"}
            raise HTTPException(status_code=400, detail="Event with this ID already exists")
    events_db.append(event)
    return {"message": "Event created successfully", "event": event}


@proj.delete("/events/{event_id}")
def delete_event(event_id: int, user_role: str = "participant"):
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="You are not allowed to delete events")
    for event in events_db:
        if event_id == event.id:
            events_db.remove(event)
            return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=404, detail="Event not found")