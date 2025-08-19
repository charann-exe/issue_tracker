from typing import List, Optional
from sqlalchemy.orm import Session
from . import models, schemas


def create_project(db: Session, project: schemas.ProjectCreate) -> models.Project:
	obj = models.Project(name=project.name)
	db.add(obj)
	db.commit()
	db.refresh(obj)
	return obj


def list_projects(db: Session) -> List[models.Project]:
	return db.query(models.Project).order_by(models.Project.id).all()


def create_issue(
	db: Session, project_id: int, payload: schemas.IssueCreate
) -> models.Issue:
	obj = models.Issue(
		project_id=project_id,
		title=payload.title,
		description=payload.description,
		severity=payload.severity,
	)
	db.add(obj)
	db.commit()
	db.refresh(obj)
	return obj


def get_issue(db: Session, issue_id: int) -> Optional[models.Issue]:
	return db.query(models.Issue).filter(models.Issue.id == issue_id).first()


def list_issues(db: Session, project_id: int) -> List[models.Issue]:
	return (
		db.query(models.Issue)
		.filter(models.Issue.project_id == project_id)
		.order_by(models.Issue.id)
		.all()
	)


def update_issue(
	db: Session, issue: models.Issue, payload: schemas.IssueUpdate
) -> models.Issue:
	data = payload.model_dump(exclude_unset=True)
	for key, value in data.items():
		setattr(issue, key, value)
	db.add(issue)
	db.commit()
	db.refresh(issue)
	return issue

