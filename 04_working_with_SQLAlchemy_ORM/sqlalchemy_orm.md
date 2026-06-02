# FastAPI & SQLAlchemy ORM

## 1. The Need for Database Integration
Hardcoding data in an application presents several critical limitations for real-world scenarios:
- **No Scalability:** Hard to implement search, filtering, or advanced reporting.
- **Lack of Concurrency:** Multiple users cannot share or access the same data simultaneously.
- **Data Loss:** All hardcoded or in-memory data is completely lost every time the server restarts.

*Integrating a database solves these issues by ensuring data is persistent and can be retrieved dynamically.*

---

## 2. What is ORM?
**ORM (Object-Relational Mapping)** is a technique that bridges the gap between Python classes and relational database tables. 
- It allows developers to interact with the database using familiar Python objects and methods instead of writing raw SQL queries.
- It abstracts away the complex database layer, significantly speeding up the development process.

---

## 3. ORM vs. Raw SQL
Consider the scenario of adding a new event to a database.

### Without ORM (Raw SQL)
Requires database-specific syntax (e.g., MySQL syntax might differ slightly from PostgreSQL or Oracle).
```sql
INSERT INTO events (title, organizer, date) 
VALUES ("Hackathon", "Alice", "2025-09-01");
```

### With ORM (SQLAlchemy)
A unified, database-agnostic approach using Python syntax.
```python
new_event = Event(title="Hackathon", organizer="Alice", date="2025-09-01")
db.add(new_event)
db.commit() 
```

---

## 4. Key Advantages of Using ORM
- **Easier Maintenance:** Pythonic syntax makes the code much easier to read and maintain.
- **Database-Agnostic:** You can seamlessly switch between different databases (e.g., SQLite to MySQL) without needing to rewrite any queries.
- **Enhanced Security:** Automatically escapes values, which significantly reduces the risk of SQL injection attacks.