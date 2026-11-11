from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, Field
from app.data import PROFILE, PROJECTS

app = FastAPI(title="Developer Portfolio API", version="1.0.0")
app.mount("/static", StaticFiles(directory="static"), name="static")


class ContactMessage(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    message: str = Field(min_length=10, max_length=2000)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home():
    with open("static/index.html", encoding="utf-8") as page:
        return page.read()


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "developer-portfolio-api"}


@app.get("/api")
async def overview():
    return {"name": app.title, "version": app.version, "docs": "/docs"}


@app.get("/api/profile")
async def profile():
    return PROFILE


@app.get("/api/projects")
async def projects():
    return {"count": len(PROJECTS), "projects": PROJECTS}


@app.get("/api/projects/{project_id}")
async def project_detail(project_id: str):
    for item in PROJECTS:
        if item["id"] == project_id:
            return item
    raise HTTPException(status_code=404, detail="Project not found")


@app.post("/api/contact")
async def contact(message: ContactMessage):
    """Validate a message; persistence and email delivery are not configured."""
    return {
        "accepted": True,
        "message": "Validated only; delivery is not configured.",
        "contact": {"name": message.name, "email": str(message.email)},
    }


@app.get("/api/stats")
async def stats():
    return {"projects": len(PROJECTS), "status": "online"}
