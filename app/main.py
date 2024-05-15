from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router import router

app = FastAPI()

# Include the router
app.include_router(router)

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")