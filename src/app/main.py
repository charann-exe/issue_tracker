from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pathlib import Path
from .database import Base, engine, get_db
from . import schemas, crud, models


# Create tables on startup for simplicity in demo project
Base.metadata.create_all(bind=engine)

app = FastAPI(title="QA-Driven Issue Tracker")

frontend_dir = Path(__file__).resolve().parent / "frontend"
if frontend_dir.exists():
	# Serve UI at /ui
	app.mount(
		"/ui",
		StaticFiles(directory=str(frontend_dir), html=True),
		name="ui",
	)


@app.post("/projects", response_model=schemas.ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
	return crud.create_project(db, project)


@app.get("/projects", response_model=list[schemas.ProjectRead])
def list_projects(db: Session = Depends(get_db)):
	return crud.list_projects(db)


@app.post(
	"/projects/{project_id}/issues",
	response_model=schemas.IssueRead,
	status_code=status.HTTP_201_CREATED,
)
def create_issue(project_id: int, payload: schemas.IssueCreate, db: Session = Depends(get_db)):
	# ensure project exists
	projects = {p.id for p in crud.list_projects(db)}
	if project_id not in projects:
		raise HTTPException(status_code=404, detail="Project not found")
	return crud.create_issue(db, project_id, payload)


@app.get("/projects/{project_id}/issues", response_model=list[schemas.IssueRead])
def list_issues(project_id: int, db: Session = Depends(get_db)):
	return crud.list_issues(db, project_id)


@app.get("/issues/{issue_id}", response_model=schemas.IssueRead)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
	issue = crud.get_issue(db, issue_id)
	if not issue:
		raise HTTPException(status_code=404, detail="Issue not found")
	return issue


@app.patch("/issues/{issue_id}", response_model=schemas.IssueRead)
def update_issue(issue_id: int, payload: schemas.IssueUpdate, db: Session = Depends(get_db)):
	issue = crud.get_issue(db, issue_id)
	if not issue:
		raise HTTPException(status_code=404, detail="Issue not found")
	# simple workflow validation: cannot move from Closed to other statuses
	if payload.status and issue.status == models.IssueStatus.CLOSED and payload.status != models.IssueStatus.CLOSED:
		raise HTTPException(status_code=400, detail="Closed issues cannot be reopened")
	return crud.update_issue(db, issue, payload)

