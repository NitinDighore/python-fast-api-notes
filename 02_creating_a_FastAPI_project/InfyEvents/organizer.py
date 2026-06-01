from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Organizer Operations")

# In-memory list of 3 organizers
organizers_db = ["Alice", "John", "Tech Club"]

@app.get("/organizers/")
def get_organizers():
    """Returns the list of organizers as a JSON array."""
    return organizers_db

@app.post("/organizers/")
def add_organizer(name: str):
    """Adds a new organizer name to the in-memory list (using a Query Parameter)."""
    if name in organizers_db:
        return {"error": f"Organizer '{name}' already exists."}
        
    organizers_db.append(name)
    return {"message": f"Organizer '{name}' added successfully.", "organizers": organizers_db}

@app.delete("/organizers/{name}")
def delete_organizer(name: str):
    """Removes an organizer by name from the list (using a Path Parameter)."""
    if name in organizers_db:
        organizers_db.remove(name)
        return {"message": f"Organizer '{name}' deleted successfully.", "organizers": organizers_db}
        
    return {"error": f"Organizer '{name}' not found."}

if __name__ == "__main__":
    # Starting the organizer app on port 8007 to avoid conflicts with previous apps
    uvicorn.run("organizer:app", host="localhost", port=8007, reload=True)