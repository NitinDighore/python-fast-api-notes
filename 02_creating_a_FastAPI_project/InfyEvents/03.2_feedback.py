from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Restaurant Feedback API")

# Using the POST method since this involves submitting form-like data
@app.post("/feedback")
def submit_feedback(name: str, rating: int, comments: str = ""):
    """
    Submit feedback for the restaurant.
    Takes a name, rating, and optional comments.
    """
    return {
        "message": f"Thank You {name} for your feedback!",
        "submitted_data": {
            "rating": rating,
            "comments": comments
        }
    }

if __name__ == "__main__":
    # Running on port 8004 to avoid conflicts with main.py, user.py, and book.py
    uvicorn.run("feedback:app", host="localhost", port=8004, reload=True)