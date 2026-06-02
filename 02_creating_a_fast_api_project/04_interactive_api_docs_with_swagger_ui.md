# Interactive API Docs with Swagger UI

To test an application's functionality, we need a client capable of requesting resources from the server using the GET method, as well as posting, updating, or deleting data on the server.

One of the major advantages of using FastAPI is that it automatically generates interactive API documentation without requiring any third-party tools (like Postman) to be installed. This built-in documentation helps developers and testers easily explore available endpoints, understand request and response formats, and test the APIs directly from the browser.

---

## Swagger UI

Swagger UI is the default interactive interface provided automatically for any FastAPI project. 

Using the `events.py` module from our `InfyEvents` project, we can use the Swagger UI to test the functionality of each HTTP method we implemented.

### How to Access Swagger UI
1. Start your Uvicorn server:
   ```cmd
   (proj_env) C:\InfyEvents> uvicorn events:proj --reload
   ```
2. Open your web browser and navigate to: **http://localhost:8000/docs**

### Using the Swagger UI to Test Functionality
Let us test the **Get All Events** functionality (which expects to display all events):
1. Expand the `GET /events` tab in the Swagger UI.
2. Click on the **Try it out** button.
3. Click on the **Execute** button.

**Result:**
Clicking on Execute will send the actual HTTP request to your running server. The response body will appear directly in the UI, containing all event details in JSON format. 

*You can similarly test all other functionalities (POST, PUT, PATCH, DELETE) by providing the required parameters or request bodies in their respective tabs.*

### Features of Swagger UI
* **Lists all available endpoints:** Easily see all your `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` routes.
* **Displays models:** Shows the required request formats and the expected response models.
* **Interactive testing:** Allows you to try requests directly from the browser (e.g., sending test JSON bodies or query parameters).
* **Clear results:** Shows the exact response data, response headers, and HTTP status codes (e.g., `200 OK` or `404 Not Found`).

---

## Alternative Documentation using ReDoc

Another built-in way to access the API documentation is **ReDoc**. While Swagger UI is great for interactive testing, ReDoc provides a clean, readable, reference-style view that is excellent for official documentation reading.

### How to Access ReDoc
Open your web browser and navigate to: **http://localhost:8000/redoc**

These pages are auto-generated and automatically update as your API grows. For instance, selecting the **Create Event** option on the left navigation panel of ReDoc will cleanly display the required event details (schema) needed to add a new event.