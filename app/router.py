from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

# Set up Jinja2 templates
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/book", response_class=HTMLResponse)
async def book(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/challenges", response_class=HTMLResponse)
async def challenges(request: Request):
    return templates.TemplateResponse("challenges/base.html", {"request": request})
