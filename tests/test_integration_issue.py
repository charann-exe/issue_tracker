import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def client():
	return TestClient(app)


def test_project_and_issue_flow(client):
	# create project
	resp = client.post("/projects", json={"name": "Demo"})
	assert resp.status_code == 201
	project = resp.json()

	# list projects
	resp = client.get("/projects")
	assert resp.status_code == 200
	assert any(p["name"] == "Demo" for p in resp.json())

	# create issue
	resp = client.post(
		f"/projects/{project['id']}/issues",
		json={"title": "Button not clickable", "description": "on home", "severity": "High"},
	)
	assert resp.status_code == 201
	issue = resp.json()

	# get issue
	resp = client.get(f"/issues/{issue['id']}")
	assert resp.status_code == 200

	# update issue status
	resp = client.patch(f"/issues/{issue['id']}", json={"status": "In Progress"})
	assert resp.status_code == 200

	# close issue
	resp = client.patch(f"/issues/{issue['id']}", json={"status": "Closed"})
	assert resp.status_code == 200

	# cannot reopen closed issue
	resp = client.patch(f"/issues/{issue['id']}", json={"status": "New"})
	assert resp.status_code == 400

