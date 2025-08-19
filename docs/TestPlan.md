## Test Plan

### Objective
Validate that the Issue Tracking API meets functional and non-functional requirements.

### Scope
- In-scope: CRUD flows for projects and issues, workflow rule enforcement.
- Out-of-scope: Authentication, advanced permissions, UI.

### Test Levels
- Unit tests for CRUD functions
- Integration tests for REST endpoints

### Test Environment
- Python 3.11+
- SQLite database
- CI via GitHub Actions

### Entry/Exit Criteria
- Entry: Code builds locally, unit tests pass.
- Exit: All automated tests pass; critical defects closed.

### Deliverables
- Test cases (`docs/TestCases.md`), RTM, Test Report, Defect Log.

