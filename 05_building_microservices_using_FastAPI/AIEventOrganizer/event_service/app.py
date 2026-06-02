import os
from datetime import date
import requests
from fastapi import FastAPI, Depends, HTTPException
from event_service.config import session, get_db
from event_service.models import Event
from event_service.schemas import EventCreate, EventOut

app = FastAPI(title="Event Service")

NOTIFY_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://localhost:8004")

@app.get("/", tags=["health"])
async def health():
    return {"service": "event-service", "status": "ok"}

# CREATE
@app.post("/events/", response_model=EventOut)
async def create_event(payload: EventCreate, db: session = Depends(get_db)):
    event = Event(
        title=payload.title,
        city=payload.city,
        date=payload.date,
        organizer=payload.organizer,
        organizer_email=payload.organizer_email
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    
    # Fire-and-forget notify (ignore failures)
    try:
        requests.post(f"{NOTIFY_URL}/notify/event-created", json={
            "id": event.id,
            "title": event.title,
            "city": event.city,
            "date": str(event.date),
            "organizer": event.organizer,
            "organizer_email": event.organizer_email
        }, timeout=2)
    except Exception:
        pass
    return event

# READ all
@app.get("/events/", response_model=list[EventOut])
async def list_events(db: session = Depends(get_db)):
    return db.query(Event).order_by(Event.date).all()

# READ one
@app.get("/events/{event_id}", response_model=EventOut)
async def get_event(event_id: int, db: session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# UPDATE
@app.put("/events/change/{event_id}", response_model=EventOut)
async def update_event(event_id: int, payload: EventCreate, db: session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event.title = payload.title
    event.city = payload.city
    event.date = payload.date
    event.organizer = payload.organizer
    event.organizer_email = payload.organizer_email
    db.commit()
    db.refresh(event)
    return event

# DELETE
@app.delete("/events/cancel/{event_id}")
async def delete_event(event_id: int, db: session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": f"Event {event_id} deleted"}

# UPCOMING
@app.get("/events/upcoming/", response_model=list[EventOut])
async def upcoming_events(db: session = Depends(get_db)):
    today = date.today()
    return db.query(Event).filter(Event.date >= today).order_by(Event.date).all()

# NEXT
@app.get("/events/next/", response_model=EventOut)
async def next_event(today: date | None = None, db: session = Depends(get_db)):
    today_dt = today or date.today()
    event = (
        db.query(Event)
        .filter(Event.date >= today_dt)
        .order_by(Event.date.asc())
        .first()
    )
    if not event:
        raise HTTPException(status_code=404, detail="No upcoming events")
    return event

# Today's events
@app.get("/events/today/", response_model=list[EventOut])
async def today_events(db: session = Depends(get_db)):
    today_dt = date.today()
    events = (
        db.query(Event)
        .filter(Event.date == today_dt)
        .order_by(Event.date.asc())
        .all()
    )
    if not events:
        raise HTTPException(status_code=404, detail="No events planned today")
    return events


"""
# Starting the Event Service

To launch the Event Service, open your terminal (with your virtual environment activated) and use one of the following methods:

### 1. Using Python Module Execution
```cmd
(venv) C:\AI_Event_Organizer> python -m event_service.app  
```
*Note: The `-m` option invokes the Python module to run as a standalone program.*

### 2. Using Uvicorn (Recommended for Development)
```cmd
(venv) C:\AI_Event_Organizer> uvicorn event_service.app:app --reload --port 8001
```
*Note: This starts the Uvicorn server with auto-reload enabled, making the Event Service accessible on **port 8001**.*

"""