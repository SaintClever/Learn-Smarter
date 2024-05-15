from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import json


templates = Jinja2Templates(directory="templates")
coding_examples = json.load(open("coding_examples.json", "r"))
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/book", response_class=HTMLResponse)
async def book(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "coding_examples": coding_examples})
