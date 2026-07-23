from fastapi import FastAPI

from system_health import system_info

app = FastAPI(title="Devops api")

@app.get("/hello")
def hello():
    """
    this is a custom api
    """
    return {"message": "Hello, welcome to DevOps API"}

@app.get("/metrics")
def metrics():
    """
    here we can monitor our system
    """
    return system_info()