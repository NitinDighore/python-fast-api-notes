from fastapi import FastAPI
import uvicorn

app = FastAPI(title="User Operations")

user_db = [
    (1, "john", "john@gmail.com"),
    (2, "jay", "jay@outlook.com"),
    (3, "priya", "priya123@gmail.com")
]

@app.get("/users")
def get_all_users():
    """Retrieve all user details from user_db."""
    return [{"user_id": u[0], "name": u[1], "email": u[2]} for u in user_db]

@app.get("/users/new")
def create_new_user(user_id: int, name: str, email: str):
    """
    Send details of a new user using query parameters.
    Example URL: /users/new?user_id=4&name=riyaz&email=riyaz@gmail.com
    """
    # Add the new user to the list as a tuple
    user_db.append((user_id, name, email))
    
    return {
        "New User": {
            "user_id": user_id,
            "name": name,
            "email": email
        }
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Look up user_id from user_db and return corresponding user details."""
    for u in user_db:
        if u[0] == user_id:
            return {"User Details": {"user_id": u[0], "name": u[1], "email": u[2]}}
    
    return {"error": f"User ID {user_id} is not found"}

if __name__ == "__main__":
    # Starting this specific app on port 8001 to avoid conflicts with main.py if both are running
    # We pass the app as an import string ("user:app") ("filename:variable") instead of the app object directly.
    # This is REQUIRED when using reload=True because Uvicorn spawns new worker processes 
    # to restart the server on code changes, and it needs the string to dynamically import the app.
    uvicorn.run("user:app", host="localhost", port=8001, reload=True)