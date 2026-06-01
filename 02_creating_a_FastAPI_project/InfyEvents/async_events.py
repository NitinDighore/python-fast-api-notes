from fastapi import FastAPI
import uvicorn
import asyncio

app = FastAPI(title="Async Event API")

events_db = [
    {"id": 1, "title": "AI Bootcamp", "city": "Bangalore"},
    {"id": 2, "title": "AI Webinar 2025", "city": "Chennai"}
]

# ---------------------------------------------------------
# Asynchronous Path Operation
# ---------------------------------------------------------
@app.get("/events")
async def get_all_events():
    """
    Fetch all events asynchronously.
    
    We use asyncio.sleep(3) to simulate a time-consuming database operation.
    Because this is an `async def` function and we `await` the sleep, 
    the FastAPI server will NOT block. It can serve other incoming requests 
    while waiting for these 3 seconds to pass.
    """
    print("Starting database query for all events...")
    
    # Simulating a slow database I/O task (non-blocking)
    await asyncio.sleep(3) 
    
    print("Database query finished!")
    return events_db

@app.get("/ping")
async def ping():
    return {"message": "Pong! I didn't get blocked by the slow events query!"}

if __name__ == "__main__":
    uvicorn.run("async_events:app", host="localhost", port=8006, reload=True)