from fastapi import FastAPI
import uvicorn
import asyncio
import random

app = FastAPI(title="Weather Tracker API")

@app.get("/temperature")
async def get_temperature():
    """
    Fetches simulated temperature data.
    Simulates a sensor delay and returns a random temperature.
    """
    # Step 1: Simulate sensor tracking by waiting for 2 seconds asynchronously
    await asyncio.sleep(2)
    
    # Step 2: Return the random temperature (20–35 °C)
    temperature = random.randint(20, 35)
    
    return {"temperature_celsius": temperature, "message": "Sensor reading successful"}

if __name__ == "__main__":
    # Starting the weather tracker app on port 8008 to avoid conflicts
    uvicorn.run("weather_tracker:app", host="localhost", port=8008, reload=True)