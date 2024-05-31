from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .router import router
import os

app = FastAPI()

# Include the router
app.include_router(router)

# Ensure the static directory exists
static = os.path.join(os.path.dirname(__file__), "static")

# Mount the static files directory
app.mount("/static", StaticFiles(directory=static), name="static")
