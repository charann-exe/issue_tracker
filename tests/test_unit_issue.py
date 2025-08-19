from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app import crud, schemas


def setup_memory_db():
	engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
	TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
	Base.metadata.create_all(bind=engine)
	return TestingSessionLocal


def test_create_and_list_projects():
	Session = setup_memory_db()
	db = Session()
	try:
		p = crud.create_project(db, schemas.ProjectCreate(name="Alpha"))
		assert p.id == 1
		projects = crud.list_projects(db)
		assert len(projects) == 1 and projects[0].name == "Alpha"
	finally:
		db.close()


def test_create_issue_and_update():
	Session = setup_memory_db()
	db = Session()
	try:
		proj = crud.create_project(db, schemas.ProjectCreate(name="Alpha"))
		issue = crud.create_issue(
			db, proj.id, schemas.IssueCreate(title="Bug 1", description="desc")
		)
		assert issue.id == 1
		updated = crud.update_issue(db, issue, schemas.IssueUpdate(title="Bug 1 fixed"))
		assert updated.title == "Bug 1 fixed"
	finally:
		db.close()

