import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from schema import EventSchema
from models import Event
from config import session, get_db
from datetime import date
from sqlalchemy import func, extract, or_

proj = FastAPI(title="AI Event Assistant")

@proj.post('/events/add')
def create_event(event: EventSchema, db: session = Depends(get_db)):
    new_event = Event(**event.__dict__)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Event created successfully", "event": new_event}

@proj.get("/events")
def get_all_events(db: session = Depends(get_db)):
    return db.query(Event).all()

@proj.get("/events/upcoming")
def upcoming_events(db: session = Depends(get_db)):
    today = date.today()
    upcoming = db.query(Event).filter(Event.date >= today).order_by(Event.date).all()
    return {"upcoming_events": upcoming}

@proj.get("/events/popular")
def popular_events(db: session = Depends(get_db)):
    popular = db.query(Event).order_by(Event.participants.desc()).limit(3).all()
    return {"popular_events": popular}

@proj.get("/events/search")
def search_events(keyword: str, db: session = Depends(get_db)):
    results = db.query(Event).filter(or_(Event.title.contains(keyword), Event.description.contains(keyword))).all()
    return {"search_results": results}

@proj.get("/events/{event_id}")
def get_event(event_id: int, db: session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"event details": event}

@proj.get("/events/monthly/{year}")
def get_monthly_events(year: int, db: session = Depends(get_db)):
    results = db.query(
        extract('month', Event.date).label('month'),
        func.count(Event.id).label('count')
    ).filter(
        extract('year', Event.date) == year
    ).group_by(
        extract('month', Event.date)
    ).all()
    return [{"month": int(r.month), "count": r.count} for r in results]

@proj.put("/events/change/{event_id}")
def update_event(event: EventSchema, db: session = Depends(get_db)):
    upd_event = db.query(Event).filter(Event.id == event.id).first()
    if not upd_event:
        raise HTTPException(status_code=404, detail="Event not found")
    upd_event.id = event.id
    upd_event.title = event.title
    upd_event.date = event.date
    upd_event.organizer = event.organizer
    upd_event.city = event.city
    upd_event.email = event.email
    db.commit()
    db.refresh(upd_event)
    return {"message": "Event updated", "event": upd_event}


@proj.delete("/events/cancel/{event_id}")
def cancel_event(event_id: int, db: session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()
    return {"message": f"Event with ID {event_id} cancelled"}


if __name__ == "__main__":
    # Starting the student app on port 8003
    uvicorn.run("main:app", host="localhost", port=8003, reload=True)