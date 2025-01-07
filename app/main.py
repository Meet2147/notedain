from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Set the base directory for the app
BASE_DIR = Path(__file__).resolve().parent

# Mount the static files directory
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request):
    """
    Serve the main HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})
