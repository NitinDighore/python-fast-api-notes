from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Book Info API")

books = [
    {"id": 1, "title": "Python Basics", "author": "Guido"},
    {"id": 2, "title": "FastAPI Deep Dive", "author": "Tiangolo"},
]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Returns details of a specific book by its ID (Path Parameter)."""
    for book in books:
        if book["id"] == book_id:
            return book
            
    return {"error": f"Book with ID {book_id} not found"}

@app.get("/search")
def search_books(author: str):
    """Filters and returns books by author name (Query Parameter)."""
    # Using a list comprehension to find matching books (case-insensitive)
    filtered_books = [book for book in books if book["author"].lower() == author.lower()]
    
    return filtered_books if filtered_books else {"message": f"No books found for author '{author}'"}

if __name__ == "__main__":
    # Running on port 8002 to avoid conflicts with main.py (8000) and user.py (8001)
    # Passing the app as an import string ("book:app") ("filename:variable") is mandatory when reload=True. 
    # Uvicorn uses multiprocessing for hot-reloading and needs the string to re-import the app.
    uvicorn.run("book:app", host="localhost", port=8002, reload=True)