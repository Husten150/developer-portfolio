# Developer Portfolio API

A responsive developer portfolio built with FastAPI, HTML, CSS, and JavaScript. Includes a JSON API, project showcase, API playground, and tests.

## Run locally on Windows PowerShell

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    python -m pytest -q
    uvicorn app.main:app --reload

Open http://127.0.0.1:8000. API docs: http://127.0.0.1:8000/docs.

## API endpoints

- GET /api/health — health check
- GET /api — API overview
- GET /api/profile — profile
- GET /api/projects — project list
- GET /api/projects/{project_id} — project detail
- POST /api/contact — contact validation
- GET /api/stats — project statistics

Contact currently validates input only; it does not save messages or send email.

## Render deployment

Create a Python Web Service connected to this repository. Build command: pip install -r requirements.txt. Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT. Verify /api/health after deployment.

## Featured repositories

- https://github.com/StellGuard/StellarGuard
- https://github.com/quadri40/koya-payment-reconciliation
