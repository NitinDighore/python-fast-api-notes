# Request and Response Models

In web development, when a client (like a browser or mobile app) sends data to a server, the **request model** defines the structure of the incoming data. Conversely, the **response model** defines the structure of the data the server sends back to the client.

## Event Organizer Assistant Scenario

* **Request Model:** Describes how a client sends details like event title, organizer, city, email, and date.
* **Response Model:** Ensures that when the server responds (e.g., confirming event creation), the client receives the data in a predictable format, typically JSON.

---

## Response Models

There are various response types that can be configured for each endpoint.

### 1. JSON Response (Default)
By default, FastAPI returns responses in JSON (JavaScript Object Notation) format. JSON is the most common data exchange format in modern APIs, represented as key-value pairs. You do not need to explicitly specify the JSON response type in your function.

### 2. Plain Text Response
Sometimes, a client may only need a quick plain text reply rather than structured JSON. FastAPI provides the `PlainTextResponse` class for this purpose, which can be configured directly in the route decorator using `response_class=PlainTextResponse`.

### 3. HTML Response
FastAPI can also return HTML content. This requires setting `response_class=HTMLResponse` in the route decorator, which is often used for rendering simple web pages directly from the server.

---

## Request Models

### Sending the Request Body as JSON
In FastAPI, a common approach to handling incoming data is to send the details inside the request body as JSON. We typically define a request model using **Pydantic classes**. 

By defining a model that inherits from `BaseModel`, FastAPI automatically:
1. **Reads** the body of the request as JSON.
2. **Converts** the corresponding types (if possible).
3. **Validates** the data. If a field is missing or invalid (e.g., an incorrectly formatted email), FastAPI automatically returns a `422 Unprocessable Entity` validation error.
4. **Provides** the parsed data to your path operation function.

### Example Pydantic Model
```python
from pydantic import BaseModel, EmailStr

class Event(BaseModel):
    id: int
    title: str
    organizer: str
    city: str
    email: EmailStr
    date: str
```
*Note: The `EmailStr` type automatically verifies that the email provided by the client is a valid email format.*