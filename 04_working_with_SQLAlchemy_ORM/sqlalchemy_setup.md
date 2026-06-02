# FastAPI & SQLAlchemy Setup

## 1. Why SQLite?
SQLite is embedded directly in Python 3.x, meaning no external database servers need to be installed or configured.
- **Pros:** Perfect for beginners, rapid prototyping, and local development. Data is saved in a simple local file (e.g., `events.db`).
- **Cons:** Not recommended for heavy production use.

---

## 2. Installation
Install SQLAlchemy to manage your Object-Relational Mapping (ORM):
```bash
pip install sqlalchemy
```

---

## 3. Database Configuration (`config.py`)
Set up the database connection, session factory, and the dependency for FastAPI.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Define the database URL
DATABASE_URL = "sqlite:///events.db"

# 2. Create the Database Engine (check_same_thread=False allows multiple threads to share the SQLite connection)
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# 3. Create Session Factory and Base Class
session = sessionmaker(bind=engine)
Base = declarative_base()

# 4. Dependency: Get DB session securely per request
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
```

---

## 4. Defining Database Models (`models.py`)
Use SQLAlchemy to map a Python class to a database table.

```python
from sqlalchemy import Column, Integer, String, Date
from config import Base, engine

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(Date)
    organizer = Column(String)
    city = Column(String)
    email = Column(String)

# Automatically creates the database and tables if they don't already exist
Base.metadata.create_all(bind=engine)
```

---

## 5. Integrating Pydantic for Validation (`schema.py`)
To cleanly separate database logic from API validation, use **Pydantic** for schemas and **SQLAlchemy** for models.

* **Pydantic Schema:** Validates incoming JSON API requests and outgoing responses.
* **SQLAlchemy Model:** Interacts with the database tables.

```python
from pydantic import BaseModel, EmailStr
from datetime import date

class EventSchema(BaseModel):
    id: int
    title: str
    date: date
    organizer: str
    city: str
    email: EmailStr
```