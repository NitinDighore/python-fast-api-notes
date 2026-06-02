import os
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Notification Service")

USER_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8003")

# 1. General notification route
@app.post("/notify/")
def notify_upcoming_events():
    """Triggers a global notification to users regarding upcoming events."""
    return {"message": "Global notification broadcast triggered for upcoming events."}

# 2. Notify specific user
@app.post("/notify/{user_id}")
def notify_user(user_id: int):
    """Triggers a notification to a specific user by their ID."""
    user = None
    
    try:
        user = requests.get(f"{USER_URL}/users/{user_id}").json()
    except Exception:
        pass
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Notification sent to {user['email']}"}

# 3. Notify by city using Query Parameter
@app.post("/notify/all")
def notify_all_by_city(city: str):
    """Notifies all users located in a specified city (e.g., /notify/all?city=Delhi)."""
    users_by_city = []
    
    try:
        users_by_city = requests.get(f"{USER_URL}/users/city/{city}").json()
    except Exception:
        pass
    
    if not users_by_city:
        raise HTTPException(status_code=404, detail="No users found in the specified city")

    notified_users = [u['email'] for u in mock_user_db.values() if u['city'].lower() == city.lower()]
    
    return {"message": f"Notifications sent to all users in {city}", "emails_notified": notified_users}