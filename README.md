## QA-Driven Issue Tracker (End-to-End SDLC/STLC Project)

This is a small but complete Issue Tracking system built to showcase the full software lifecycle end to end. It demonstrates requirements analysis, design, coding, testing, code reviews, documentation, test case execution, test reporting, defect lifecycle management, and status reporting.

### Tech Stack
- FastAPI (Python) for REST API
- SQLite + SQLAlchemy for persistence
- Pytest for unit/integration tests
- GitHub Actions CI for automated test runs
- Static Web UI (HTML/CSS/JS) served at `/ui`

### Features
- Create and list projects
- Create, list, view, and update issues (status, severity)
- Simple defect workflow: New → In Progress → Resolved → Closed (closed issues cannot be reopened)
- Interactive docs at `/docs` and a simple web UI at `/ui`

### Install and run (Windows PowerShell)
```powershell
# 1) Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run tests (unit + integration)
pytest -q

# 4) Start the API
uvicorn app.main:app --reload --port 8000 --app-dir src
```

Then open:
- API Docs (Swagger UI): http://127.0.0.1:8000/docs
- Simple Web UI: http://127.0.0.1:8000/ui

### API (quick glance)
- POST `/projects` { name }
- GET `/projects`
- POST `/projects/{project_id}/issues` { title, description, severity }
- GET `/projects/{project_id}/issues`
- GET `/issues/{issue_id}`
- PATCH `/issues/{issue_id}` { status?, title?, description?, severity? }

### Quick examples (PowerShell + curl.exe)
```powershell
# Create a project
curl.exe -s -X POST http://127.0.0.1:8000/projects -H "Content-Type: application/json" -d "{\"name\":\"Demo\"}"

# List projects
curl.exe -s http://127.0.0.1:8000/projects

# Create an issue (replace 1 with your project id)
curl.exe -s -X POST http://127.0.0.1:8000/projects/1/issues -H "Content-Type: application/json" -d "{\"title\":\"Bug\",\"description\":\"Home page\",\"severity\":\"High\"}"

# Update an issue status
curl.exe -s -X PATCH http://127.0.0.1:8000/issues/1 -H "Content-Type: application/json" -d "{\"status\":\"In Progress\"}"
```

### Documentation
See `docs/` for:
- `SRS.md` (requirements)
- `Architecture.md` (design)
- `TestPlan.md`, `TestCases.md`, `RTM.md`
- `DefectLifecycle.md`, `DefectLog.md`
- `TestReport.md`, `StatusReports/WeeklyReport_Week1.md`
- `CodeReview.md`, `ReviewChecklist.md`

These artifacts are resume-ready and map directly to the listed skills.

### Project structure
```
.
├─ src/
│  └─ app/
│     ├─ main.py
│     ├─ database.py
│     ├─ models.py
│     ├─ schemas.py
│     ├─ crud.py
│     └─ frontend/
│        ├─ index.html
│        ├─ app.js
│        └─ styles.css
├─ tests/
│  ├─ test_unit_issue.py
│  └─ test_integration_issue.py
├─ docs/
│  ├─ SRS.md
│  ├─ Architecture.md
│  ├─ TestPlan.md
│  ├─ TestCases.md
│  ├─ RTM.md
│  ├─ TestReport.md
│  ├─ DefectLifecycle.md
│  ├─ DefectLog.md
│  ├─ CodeReview.md
│  └─ StatusReports/
│     └─ WeeklyReport_Week1.md
├─ requirements.txt
├─ pytest.ini
└─ .github/workflows/ci.yml
```

### Tips
- To reset data, stop the server and delete `app.db` in the project root.
- If running from another shell, adapt the activation command (e.g., `. .venv/bin/activate` on Linux/macOS).

### Resume bullets (example)
- Led end-to-end SDLC for an Issue Tracker API: authored SRS, architecture design, and RTM; implemented FastAPI + SQLite backend with SQLAlchemy ORM.
- Built comprehensive test suite (unit + integration) using Pytest; integrated CI for automated test execution and reporting.
- Drove STLC activities: crafted Test Plan and Test Cases, executed tests, logged/triaged defects, produced test and status reports weekly.
- Performed peer-style code reviews following a checklist; documented review findings and improvements.

