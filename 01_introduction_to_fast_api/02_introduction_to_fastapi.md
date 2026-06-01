# Introduction to FastAPI

## Getting to Know FastAPI

### What is FastAPI?
FastAPI is a modern, high-performance web framework for building APIs with Python 3.6+. Created in 2018 by Sebastián Ramírez, it allows developers to build robust, reusable applications that communicate effectively.
* **Purpose:** Acts as a "bridge" (API) enabling different programs to share information (e.g., a mobile app communicating with a restaurant's server).
* **Under the Hood:** Built on top of **Starlette** (for web routing) and **Pydantic** (for data validation).
* **Standards:** Based on open standards like **OpenAPI** and **JSON Schema**.

### Why do we need FastAPI?
Without a framework, handling requests, validating data, and returning responses must be done manually, which is slow and error-prone. FastAPI automates:
* Data validation
* Request handling speed
* Automatic API documentation creation

### Where does FastAPI fit?
In a **3-tier web application architecture**, FastAPI serves as the **backend/application tier**. It receives requests from the frontend, processes business logic, interacts with the database, and returns the response to the client.

### Who uses FastAPI?
Its high performance and features have led to its adoption by major companies, including:
* **Netflix:** Powering internal data tools.
* **Microsoft:** Running in various production services.
* **Uber:** Building high-performance APIs.
* **Explosion:** The creators of the spaCy AI library.

---

## Architecture of FastAPI
A typical FastAPI application follows a structured layered architecture:

1. **API Layer:** FastAPI endpoints that handle incoming HTTP requests.
2. **Business Logic Layer:** The core services and operations (your custom code).
3. **Data Access Layer:** Uses an ORM (like SQLAlchemy) to interact with databases.
4. **Database:** Systems like PostgreSQL, MySQL, etc.

### The Execution Stack
From top to bottom, the execution stack looks like this:
1. **Application (Custom Code):** The highest level. Includes your business logic, database queries, and defined endpoint routes.
2. **FastAPI (Web Framework):** Sits between your code and the server. Routes requests, handles data validation (via Pydantic), and generates API docs.
3. **Uvicorn (Server):** The foundational layer. It is an **ASGI (Asynchronous Server Gateway Interface)** web server that listens for external HTTP requests and asynchronously passes them to FastAPI.

---

## Key Features and Benefits

* **Easy to Read and Write:** Python-based, meaning existing Python developers can write scalable code without learning a new language.
* **Quick API Development:** Comes with predefined libraries and components.
* **Super Fast:** Highly concurrent. Handles hundreds of simultaneous requests without slowing down (like multiple bank tellers avoiding long queues).
* **Automatic Data Validation:** Prevents crashes by validating data types automatically. If a user inputs an invalid age (e.g., text instead of a number), FastAPI sends a clear error message instead of crashing.
* **Free Built-in Testing Tool:** Automatically generates a **Swagger UI** page. This acts as a playground to test your API without needing third-party tools like Postman.
* **Highly Scalable:** Suitable for simple microservices with a few lines of code, or massive, complex enterprise systems.
* **Real-time Data Handling:** Supports async I/O, easily integrating with WebSockets for real-time updates.
* **IoT Support:** Excels at handling large volumes of continuous data inputs from sensors and smart devices.

---

## Use Cases and Applications

* **Data-Driven Applications:** Live dashboards sharing real-time data across systems.
* **Chatbots and Virtual Assistants:** Connecting chat interfaces to backend logic (e.g., order status checking).
* **E-Commerce Platforms:** Processing customer orders, cart updates, and inventory tracking.
* **AI and Machine Learning:** Serving ML models (e.g., a housing price predictor receiving parameters and returning estimates).
* **Internet of Things (IoT):** Collecting data from temperature sensors to adjust smart home AC systems.
* **Microservices Architecture:** Breaking down giant monolithic apps into independent, scalable services (e.g., separating login, payments, and product catalogs).

---

## Comparison: Flask vs. FastAPI

| Feature              | Flask                               | FastAPI                                        |
| **Ease of Use**      | Simple and easy to start            | Simple but more structured                     |
| **Speed**            | Fast enough for small projects      | Much faster, built for bigger projects         |
| **Data Checking**    | Manual validation required          | Done automatically (via Pydantic)              |
| **Built-in Testing** | Not available by default            | Automatically available (Swagger UI)           |
| **When to Use**      | Good for small websites or learning | Great for APIs, data apps, and larger projects |

---

## Interview Questions

**Q1: What is FastAPI and what are the main tools it is built upon?**
**Answer:** FastAPI is a modern, high-performance Python web framework used for building APIs. It is built under the hood using **Starlette** (for asynchronous web routing) and **Pydantic** (for data validation).

**Q2: Who created FastAPI and in what year was it launched?**
**Answer:** FastAPI was created by Sebastián Ramírez and was launched in 2018.

**Q3: How does FastAPI handle data validation?**
**Answer:** FastAPI uses Pydantic models to automatically validate incoming data types. If a user provides invalid data (like sending text instead of an expected integer), FastAPI catches it automatically and returns a clear, structured JSON error message without crashing the application.

**Q4: What is Uvicorn, and why is it needed in a FastAPI project?**
**Answer:** Uvicorn is an ASGI (Asynchronous Server Gateway Interface) web server. While FastAPI is the web framework that handles routing and logic, Uvicorn acts as the foundational server layer that actually listens for external HTTP requests and passes them asynchronously to FastAPI.

**Q5: What are the three layers of the FastAPI execution stack?**
**Answer:** From top to bottom, the stack is:
1. **Application Layer:** Your custom Python code and business logic.
2. **FastAPI Layer:** The web framework handling routing and data validation.
3. **Uvicorn Layer:** The web server listening for outside HTTP requests.

**Q6: Explain what open standards FastAPI is based on.**
**Answer:** FastAPI is built entirely on open standards, specifically **OpenAPI** (for API definitions and documentation) and **JSON Schema** (for defining data structures).

**Q7: What is Swagger UI in the context of FastAPI?**
**Answer:** Swagger UI is an interactive API documentation interface that FastAPI generates automatically. It acts as a built-in testing page or "playground" where developers can test their API endpoints directly from the web browser without needing external tools like Postman.

**Q8: In a traditional 3-tier web architecture, where does FastAPI fit?**
**Answer:** FastAPI fits into the **Application / Service Tier (Backend)**. It sits between the Presentation Tier (Frontend/UI) and the Persistence Tier (Database), receiving requests from users, processing business rules, querying the database, and returning responses.

**Q9: What are some major companies that use FastAPI in production?**
**Answer:** FastAPI is utilized by large tech companies including Netflix (for internal data tools), Microsoft, Uber (for high-performance APIs), and Explosion (creators of the spaCy library).

**Q10: What makes FastAPI a better choice than Flask for modern API development?**
**Answer:** While Flask is great for small websites and learning, FastAPI is much faster, natively supports asynchronous programming, automatically handles data validation, and generates interactive API documentation out-of-the-box.

**Q11: FastAPI was built using the following tool.**
**Answer:** Starlette

**Q12: FastAPI was created in which year?**
**Answer:** 2018