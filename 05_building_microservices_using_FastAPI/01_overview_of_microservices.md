# Microservices & FastAPI: Cheat Sheet

## 1. What are Microservices?
A software architecture design where a large application is broken into **small, independent services**.
* **Focused:** Each service handles a specific business function.
* **Communication:** Services interact via well-defined APIs (HTTP, gRPC, or message queues).
* **Independent:** They can be developed, deployed, and scaled without affecting the rest of the system.

## 2. Core Advantages
* **Loose Coupling:** Changes in one service don't require redeploying the entire system.
* **Independent Scaling:** Scale only the parts of the app with high traffic (e.g., just the Event search).
* **Fault Isolation:** If a minor service fails (like notifications), users can still browse the core app.
* **Faster Development:** Multiple teams can work simultaneously on different services.

## 3. Why FastAPI for Microservices?
* **Lightweight & Fast:** Emphasizes simplicity, speed, and high performance.
* **Type Hints & Validation:** Built-in data validation for request/response models.
* **Async Support:** Natively supports asynchronous programming for high concurrency.
* **Auto-Documentation:** Automatically generates interactive API documentation.

## 4. Case Study: AI Event Organizer
Breaking a monolithic app into a scalable microservices ecosystem:
* **Event Service:** Manages event data (CRUD operations, upcoming events lists).
* **Assistant Service:** Handles AI queries (e.g., "Next event", "Events in Bangalore").
* **User Service (Future):** Manages participants, authentication, and login.
* **Notification Service (Future):** Sends email reminders asynchronously.

## 5. Microservice Design Patterns & Principles

### Architecture Fundamentals
* **High Cohesion:** A service should have **one** specific responsibility (e.g., Event Service only manages events, not emails).
* **Loose Coupling:** Services use APIs to communicate but do not depend on each other's internal logic.

### Service-to-Service Communication
* **Synchronous (Direct Call):** One service waits for a response (using REST or gRPC). Good for immediate, non-blocking data lookups.
* **Asynchronous (Event-Driven):** Uses message brokers (Kafka, RabbitMQ). A service publishes an event and moves on without waiting. Ideal for IO-bound/blocking operations like sending emails.

### Resilience & Reliability
In distributed systems, failures will happen. Protect the system using:
* **Timeouts:** Avoid waiting forever for a response.
* **Retries with Backoff:** Reattempt failed requests after increasing delays.
* **Circuit Breaker:** Temporarily block requests to a failing service to prevent cascading failures or overloading.

### Consistency Models
Managing state across multiple databases:
* **Strong Consistency:** All users see the updated data immediately. Can increase latency because the system locks until sync is complete.
* **Eventual Consistency:** Data syncs across systems after a short delay. Highly scalable and typical in modern microservices (e.g., an event is created, and it appears in the AI Assistant's queue a few seconds later).