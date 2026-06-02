# Path and Query Parameters

When building web applications and APIs, we frequently need to send information from the client to the server. Two of the most common ways to achieve this in REST APIs are:

1. **Path Parameters:** Values embedded directly in the URL path, primarily used to identify a specific, unique resource.
2. **Query Parameters:** Optional key-value pairs appended after the `?` symbol in the URL (as a query string), typically used to filter, sort, or modify the resource.

---

## Path Parameters

Path parameters capture dynamic values directly from the URL. They are most commonly used to fetch or manipulate a specific resource (like an event by its ID, organizer, or city).

### Example
In our AI Assistant Event Organizer, if we want to retrieve details of a single event identified by a unique `event_id`, we can include it directly in the URL path:

```python
from fastapi import FastAPI

proj = FastAPI()

@proj.get("/events/{event_id}")
def read_event(event_id: int):
    return {"event_id": event_id}
```
*(Note: By default, FastAPI returns responses in JSON format, which is represented as a set of key-value pairs similar to a Python dictionary.)*

### How it works
* **Dynamic Routing:** `{event_id}` acts as a dynamic path parameter.
* **Automatic Conversion:** When a user requests `http://localhost:8000/events/123`, FastAPI automatically converts the `"123"` from the URL into an `int`.
* **Automatic Validation:** Because we defined the type hint as `int` (`event_id: int`), FastAPI implicitly performs type checking. If a user passes a non-integer value (e.g., `http://localhost:8000/events/e1`), FastAPI automatically returns a structured validation error message instead of crashing the server.

---

## Query Parameters

Unlike path parameters, query parameters are specified as `key=value` pairs after the `?` in the URL. Multiple parameters can be chained together using an `&`. They are ideal for filtering or customizing responses without pointing to one exact resource.

### Example
Suppose we want to fetch events based on a specific `topic` and a specific `city`. Instead of creating dozens of separate paths, we use query parameters:

```python
from fastapi import FastAPI

proj = FastAPI()

@proj.get("/search")
def search_events(topic: str, city: str = "Bangalore"):
    return {"topic": topic, "city": city}
```
* In this code, `topic` is a **mandatory** parameter because it lacks a default value.
* `city` is an **optional** parameter. If the client does not provide it, it defaults to `"Bangalore"`.

### Query Parameter Scenarios

Let's look at how FastAPI handles different client requests based on the code above:

**Scenario 1: Provide all parameters**
* **URL:** `http://localhost:8000/search?topic=ai&city=chennai`
* **Behavior:** Both `topic` and `city` are provided.
* **Output:** `{"topic": "ai", "city": "chennai"}`

**Scenario 2: Omit optional parameters**
* **URL:** `http://localhost:8000/search?topic=ai`
* **Behavior:** `topic` is provided, but `city` is omitted. FastAPI automatically uses the default value.
* **Output:** `{"topic": "ai", "city": "Bangalore"}`

**Scenario 3: Omit mandatory parameters**
* **URL:** `http://localhost:8000/search`
* **Behavior:** The mandatory `topic` parameter is missing.
* **Output:** FastAPI throws a `422 Unprocessable Entity` error, indicating that a required query parameter is missing.