# Setting Up FastAPI

## The Need for Virtual Environments
When working on multiple Python projects, each might require different versions of packages (like FastAPI) or even Python itself. To avoid version conflicts, we use **virtual environments** to keep dependencies completely isolated per project.

**Example Scenario:** We are building an application called "FirstApp" to help company event organizers manage hackathons, webinars, and other activities. To start building this application, we first need to set up our isolated environment.

---

## Managing a Virtual Environment
Here are the step-by-step instructions to create, activate, and deactivate a virtual environment:

### Step 1: Create a Project Folder
Open your command prompt or terminal, create a new directory for your project, and navigate into it:
```cmd
C:\> mkdir FirstApp
C:\> cd FirstApp
```

### Step 2: Create the Virtual Environment
Create a virtual environment (named `environment` here) which will act as the library root for all the packages needed for this specific project.
```cmd
C:\FirstApp> python -m venv environment
```

### Step 3: Activate / Deactivate the Environment
Before installing FastAPI or any dependencies, you must **activate** the virtual environment. 
```cmd
C:\FirstApp> environment\Scripts\activate
```
Once activated, your terminal prompt will change to show the environment name, like this: `(environment) C:\FirstApp>`.

When you are done working and want to exit the isolated environment, you can **deactivate** it:
```cmd
(environment) C:\FirstApp> environment\Scripts\deactivate
```

> **Note:** If you are using an IDE like **PyCharm**, a virtual environment (usually named `venv`) is automatically created and activated for you when you start a new project. You can skip the steps above and proceed directly to installation.

---

## Installing FastAPI

Once your virtual environment is active, you can install FastAPI along with its standard dependencies using `pip`:
```cmd
(environment) C:\FirstApp> pip install fastapi[standard]
```

### Alternative Installation (Best Practice)
A standard best practice in Python development is to list all project dependencies in a `requirements.txt` file. This makes it easier to share the project with others, track dependencies, or deploy the application.

1. Create a file named `requirements.txt` in your project folder and add the required packages:
```text
fastapi
pydantic[email]
uvicorn
sqlalchemy
```

2. Run the following command to install all the dependencies in one go:
```cmd
(environment) C:\FirstApp> pip install -r requirements.txt
```

## Commonly Used Environment & FastAPI Commands 

Once your environment is set up and packages are installed, you will frequently use the following commands:

### Viewing Installed Packages 

To see a list of all packages currently installed in your virtual environment:
```cmd
(environment) C:\FirstApp> pip list
```

### Saving Dependencies
To generate or update a `requirements.txt` file with the exact versions of all installed packages:
```cmd
(environment) C:\FirstApp> pip freeze > requirements.txt
```

### Running the FastAPI Server
To start the Uvicorn development server (assuming your main FastAPI code is in a file named `main.py` and the FastAPI instance is named `app`):
```cmd
(environment) C:\FirstApp> uvicorn main:app --reload
```
*(The `--reload` flag tells the server to restart automatically whenever you make code changes).*

### Deleting Installed Packages
If you need to remove a specific package, you can uninstall it using:
```cmd
(environment) C:\FirstApp> pip uninstall <package_name>
```
*(You will be prompted to confirm the deletion. You can bypass the prompt by adding `-y` to the command).*

To uninstall **all** packages listed in your `requirements.txt` file at once:
```cmd
(environment) C:\FirstApp> pip uninstall -r requirements.txt -y
```