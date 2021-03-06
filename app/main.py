from fastapi import FastAPI, HTTPException
from message import regards
from pydantic import BaseModel

app = FastAPI() # Create a FastAPI instance

@app.get("/") # Create a path operation (HTTP methods)
def root(): # Define the path operation function
    return {"message": regards("root")} # Return a JSON

@app.get("/name", description="Return hello message to the user")
def get_name(input_name):
    return {"message": "Hello " + input_name + ", Welcome!"}

@app.get("/two_power")
def two_power(number: int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Must enter a positive integer or 0")
    return {"result": 2**number}

@app.get("/three_power/{power}")
def three_power(power: int):
    return {"result": 3**power}

class inputs(BaseModel):
    base: int
    power: int

@app.post("/power")
def power(data: inputs):
    return ({
      "data": [data.base, data.power],
      "result": data.base**data.power  
    })
