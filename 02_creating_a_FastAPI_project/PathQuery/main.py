from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
import os

proj = FastAPI(title="AI Event Assistant")

@proj.get("/",response_class=HTMLResponse)
def homepage():
    return """<h1>Welcome to the AI Event Assistant!</h1>
    You can Organize, manage, and register for company events 
    like hackathons, webinars, sports, and more.
    <br><br>Start exploring now!"""

"""
--- Path Parameters ---
- Path parameters capture dynamic values directly from the URL path (e.g., {event_id}).
- They are mostly used to identify, fetch, or manipulate a specific, unique resource.
- By defining the type hint (e.g., event_id: int), FastAPI implicitly validates and converts the data.
- If a user passes an incorrect type (like a string 'e1' instead of an integer), FastAPI automatically catches it and returns an error response.
"""
@proj.get("/events/{event_id}")
def read_event(event_id: int):
    return {"event_id": event_id}
  
@proj.get("/welcome/{organizer_name}")
def welcome_organizer(organizer_name: str):
    return f"Welcome {organizer_name} to Event Organizer Portal!"

"""
--- Query Parameters ---
- Query parameters are optional key-value pairs appended after the '?' symbol in the URL (e.g., /search?topic=ai&city=chennai).
- They are commonly used to filter, search, or customize the response.
- Multiple query parameters can be chained together using the '&' symbol.
- A parameter without a default value is mandatory (e.g., topic).
- A parameter with a default value is optional (e.g., city defaults to "Bangalore" if omitted).
"""
@proj.get("/search")
def search_events(topic: str, city: str = "Bangalore"):
    return {"topic": topic, "city": city}

@proj.get("/event-count")
def count_events(year: int):
    # Returning a hardcoded response as per the exercise instructions
    return f"Number of events planned in {year}: 5"

if __name__=="__main__":
    # We pass the FastAPI instance `proj` directly here.
    # This is suitable when we are NOT using reload=True or multiple workers.
    # (Uvicorn runs the app completely within the current Python process).
    uvicorn.run(proj, host="localhost", port=8000)