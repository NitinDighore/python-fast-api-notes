from fastapi import FastAPI, HTTPException, Depends
from event_service.config import session, get_db
from event_service.models import User
from event_service.schemas import UserRegistration

app = FastAPI(title="User Service")

# 1. Basic registration route
@app.post("/users/")
def register_user_basic(name: str, email: str, db: session = Depends(get_db)):
    """Register a user by capturing basic details via query parameters."""
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully", "user_id": user.id, "name": user.name}

# 2. Secure registration route with Pydantic validation
@app.post("/users/register")
def register_user_secure(user: UserRegistration, db: session = Depends(get_db)):
    """Register a user using a JSON body with strong password validation."""
    user = User(name=user.name, email=user.email, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return

# 3. Subscribe user to an event
@app.post("/users/{user_id}/subscribe")
def subscribe_user(user_id: int, event_name: str, db: session = Depends(get_db)):
    """Subscribe a specific user to an event."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.event_name = event_name
    db.commit()
    db.refresh(user)
    return {"message": "User subscribed to the event successfully"}

# 4. Get user details
@app.get("/users/{user_id}")
def get_user_details(user_id: int, db: session = Depends(get_db)):
    """Retrieve details of a specific user."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.id, "name": user.name, "email": user.email, "event_name": user.event_name}

@app.get("/users/city/{city}")
def get_users_by_city(city: str, db: session = Depends(get_db)):
    users = db.query(User).filter(User.city == city).all()
    return {"users": [{"id": user.id, "name": user.name, "email": user.email} for user in users] }