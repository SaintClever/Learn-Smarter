from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
coding_examples = json.load(open("coding_examples.json", "r"))

router = APIRouter()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/book", response_class=HTMLResponse)
def book(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "coding_examples": coding_examples})


app.include_router(router)