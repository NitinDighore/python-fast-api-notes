# Case Study: AI Assistant Event Organizer

## Introduction
In today’s digital age, event management can go beyond manual scheduling and static calendars. By leveraging Artificial Intelligence (AI) and modern web frameworks, we can build intelligent assistants that not only store event details but also answer natural language queries (e.g., *“What is the next event?”* or *“Show me all events organized by John”*).

The **AI Assistant Event Organizer** is a practical case study that demonstrates how to integrate AI-like query processing with a simple event management system. 

This project combines several core concepts:
* **Backend Development:** Using FastAPI.
* **Data Handling:** Using SQLite database through SQLAlchemy ORM.
* **Data Validation:** Using Pydantic.
* **Microservices Design:** Separating the event management logic from the AI assistant logic.
* **Natural Query Interpretation:** Mimicking how intelligent systems like Alexa, Siri, or Google Assistant respond to users.

## Problem Statement
Imagine a small organization that frequently conducts workshops, webinars, and team activities. The details (title, date, organizer, etc.) are stored digitally. Employees often ask plain-English questions such as:
* *“What events are coming up this week?”*
* *“List all the events organized by John.”*
* *“Tell me the next scheduled event.”*

**The Challenge:** Traditionally, answering these questions requires manually searching through a calendar or database, which is time-consuming and lacks user-friendliness.

**The Goal:** Build an application allowing users to interact with an assistant that understands natural language queries and returns the required information instantly.

---

## Case Study: Objectives & Architecture

This system utilizes a **Microservices Architecture**, splitting the application into two smaller, simpler services that work together rather than one large complex monolith. 

### 1. The Event Service
This service is strictly responsible for managing event data.
* **Functionality:** Create, update, delete, and retrieve events.
* **Data Stored:** Event ID, title, organizer, city, and date.
* **Endpoints:** Includes specialized endpoints like checking for upcoming events or searching by specific fields (e.g., title or city).

### 2. The Assistant Service
This service handles user interaction and natural language processing.
* **Functionality:** Accepts user queries in plain English.
* **Processing:** Interprets the query and decides exactly which API endpoint of the Event Service to call.
* **Output:** Returns a friendly, conversational response (e.g., *"The next event is AI Workshop on 2025-09-10 organized by Jane."*).

### 3. Benefits of this Microservices Integration
* **Scalability & Maintenance:** Both services are kept separate, making the system modular and easier to maintain.
* **Separation of Concerns:** The Event service focuses solely on data; the Assistant service focuses solely on orchestration and intent.
* **Future-proofing:** The assistant service can be upgraded later to use a real AI/NLP model (like OpenAI) without needing to rewrite how the Event Service operates.

---

## AI Assistant Queries - Examples

To understand how the Assistant Service interprets natural language, here are five sample interactions:

1. **Next Event**
   * **User:** *“What is the next event?”*
   * **Action:** The assistant checks the nearest date in the event list and returns the specific event details.

2. **Upcoming Events**
   * **User:** *“Show me upcoming events.”*
   * **Action:** The assistant retrieves all events scheduled after today’s date.

3. **Events by Organizer**
   * **User:** *“List events by Infosys.”*
   * **Action:** The assistant filters the database for events where the organizer is 'Infosys' and returns those results.

4. **Events on a Specific Date**
   * **User:** *“What events are on 2025-09-10?”*
   * **Action:** The assistant searches for any events exactly matching the provided date.

5. **Count Events**
   * **User:** *“How many events are scheduled?”*
   * **Action:** The assistant calculates the total number of upcoming events and returns the count.

---

## Conclusion & Learning Outcomes

The AI Assistant Event Organizer bridges the gap between traditional database-driven management systems and modern AI-driven intelligent assistants. 

By completing this case study, learners will gain hands-on experience in:
1. Building high-performance REST APIs with FastAPI.
2. Designing and implementing a Microservices architecture.
3. Managing persistent data with databases and ORMs.
4. Implementing assistant-style intent resolution and query handling.

Ultimately, this project is an excellent starting point for understanding how real-world applications—such as intelligent chatbots and scheduling assistants—are built from the ground up.