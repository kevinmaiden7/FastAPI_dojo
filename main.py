from fastapi import FastAPI
from message import regards

app = FastAPI() # Create a FastAPI instance

@app.get("/") # Create a path operation (HTTP methods)
def root(): # Define the path operation function
    return {"message": regards("root")} # Return a JSON

@app.get("/name")
def get_name(input_name):
    return {"message": "Hello " + input_name + ", Welcome!"}