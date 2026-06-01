"""
--- Helper Notes for VS Code & Running the Server ---

1. Selecting the correct Python Interpreter in VS Code:
   - Press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
   - Search for and select "Python: Select Interpreter".
   - Click on "Enter interpreter path..." -> "Find...".
   - Navigate to your virtual environment folder (e.g., env or proj_env).
   - Go into the "Scripts" folder and select "python.exe".

2. How to run this project:
   - Method 1 (Directly with Python):
     Run `python main.py` in your terminal.
     (Note: This will not automatically reload when you change code, but it executes the `if __name__ == "__main__":` block so it reads the .env PORT variable).
   
   - Method 2 (Using Uvicorn CLI - Best for Development):
     Run `uvicorn main:proj --reload` in your terminal.
     (Note: This will automatically restart the server on code changes, but it skips the `if __name__ == "__main__":` block so the .env PORT is ignored; to change the port here, append `--port 8080`).
     
     Breakdown of `uvicorn main:proj --reload`:
     * `uvicorn`: The ASGI web server running the app.
     * `main`: The Python file name (main.py) without the .py extension.
     * `proj`: The FastAPI instance variable name (proj = FastAPI(...)).
     * `--reload`: Automatically restarts the server upon file saves.
     (Note: The uvicorn server can be stopped in the terminal by pressing Ctrl+C).


--- Code Breakdown & Concepts ---

* Uvicorn: A fast ASGI (Asynchronous Server Gateway Interface) web server. It listens for 
  incoming HTTP requests and redirects them to your FastAPI application for processing.

* `from fastapi import FastAPI`: Imports the main framework class.

* `from fastapi.responses import HTMLResponse`: Imported to explicitly tell FastAPI that 
  our endpoint will return an HTML string rather than the default JSON format.

* `proj = FastAPI(...)`: Creates the core application instance used to register all routes.

* `@proj.get('/', response_class=HTMLResponse)`: A routing decorator. It tells FastAPI to 
  listen for HTTP GET requests at the root URL ('/') and return an HTML response.

* `def homepage():`: The path operation function containing the logic that runs when the route is hit.

* `uvicorn.run(...)`: Programmatically starts the Uvicorn server on localhost at port 8000 
  when the script is run directly.
"""

from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the variables from the .env file into the environment

proj = FastAPI(title="AI Event Assistant")

@proj.get("/",response_class=HTMLResponse)
def homepage():
    return """<h1>Welcome to the AI Event Assistant!</h1>
    You can Organize, manage, and register for company events 
    like hackathons, webinars, sports, and more.
    <br><br>Start exploring now!"""

if __name__=="__main__":
    # Get the PORT from the environment, defaulting to 8000 if not found
    server_port = int(os.getenv("PORT", 8000))
    print(f"Starting server on port: {server_port}")
    uvicorn.run(proj, host="localhost", port=server_port)

"""
--- Interview Questions based on main.py ---

Q1: What is the purpose of the `FastAPI` class imported from the `fastapi` module?
Answer: It is the core application class. Instantiating it (e.g., `proj = FastAPI(...)`) creates the central application object that registers all routes, middleware, and dependencies.

Q2: What does the `@proj.get("/")` decorator do?
Answer: It defines a "path operation". It tells the FastAPI application (`proj`) to listen for HTTP GET requests directed at the root URL path (`/`) and execute the function immediately below it.

Q3: Why is `response_class=HTMLResponse` explicitly provided in the decorator?
Answer: By default, FastAPI automatically converts returned data into JSON and sets the content type to `application/json`. Providing `HTMLResponse` overrides this, telling FastAPI to return the string as raw HTML with a `text/html` content type.

Q4: What is a "path operation function" in this script?
Answer: The `homepage()` function is the path operation function. It holds the actual Python logic that FastAPI executes when the mapped route and method are requested by a client.

Q5: What does the `title="AI Event Assistant"` parameter do during FastAPI initialization?
Answer: It configures the metadata for the application. This title will be prominently displayed at the top of the automatically generated Swagger UI documentation (available at `/docs`).

Q6: What is the purpose of importing and using `uvicorn` inside the script?
Answer: Uvicorn is the ASGI web server. By importing it and calling `uvicorn.run()`, we can start the web server programmatically directly from the Python script without needing to use the command line CLI.

Q7: Why do we wrap the `uvicorn.run()` execution inside the `if __name__ == "__main__":` block?
Answer: It ensures the server only starts if the script is executed directly (e.g., `python main.py`). If this file were imported as a module into another script, the server wouldn't accidentally start.

Q8: What host and port are configured for the server in this code?
Answer: The server is bound to `localhost` (which resolves to `127.0.0.1`) and listens on port `8000`.

Q9: If you start the server from the terminal using `uvicorn main:proj --reload`, does the `uvicorn.run()` line inside the script execute?
Answer: No. When run via the Uvicorn CLI, the file is imported as a module. Therefore, the special `__name__` variable evaluates to `"main"` rather than `"__main__"`, so the block is safely bypassed.

Q10: What HTTP status code is automatically returned by the `homepage()` function when successful?
Answer: FastAPI automatically returns a `200 OK` HTTP status code upon the successful execution of a path operation function unless explicitly configured otherwise.
"""
