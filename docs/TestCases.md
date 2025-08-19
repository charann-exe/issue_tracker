## Test Cases

### TC-01 Create Project
- Precondition: API server running
- Steps: POST `/projects` with name="Alpha"
- Expected: 201 Created, JSON with id and name

### TC-02 List Projects
- Steps: GET `/projects`
- Expected: 200 OK, list contains "Alpha"

### TC-03 Create Issue
- Steps: POST `/projects/{id}/issues` with title, description, severity
- Expected: 201 Created, issue fields returned

### TC-04 Get Issue
- Steps: GET `/issues/{issue_id}`
- Expected: 200 OK, correct issue

### TC-05 Update Issue Status
- Steps: PATCH `/issues/{issue_id}` to "In Progress"
- Expected: 200 OK, status updated

### TC-06 Close Issue
- Steps: PATCH `/issues/{issue_id}` to "Closed"
- Expected: 200 OK, status Closed

### TC-07 Reopen Closed Issue (Negative)
- Steps: PATCH `/issues/{issue_id}` to "New" after closed
- Expected: 400 Bad Request, cannot reopen

